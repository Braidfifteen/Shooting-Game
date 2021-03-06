import pygame
import random
import math
import sys
 
dX = 1920
dY = 1080
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (100, 0, 100)
ORANGE = (200, 0, 20)
YELLOW = (177, 255, 10)
CYAN = (0, 255, 255)
MIDNIGHTBLUE = (25, 25, 112)
TEAL = (0, 128, 128)


class DrawText():
    def __init__(self, msg, txt_color, bg_color, x, y):
        self.message = str(msg)

        self.font = pygame.font.SysFont(None, 48)
        self.image = self.font.render(self.message, True, txt_color, bg_color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def blit(self, screen):
        screen.blit(self.image, self.rect)

        
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
      
      
class RoomDoors():
        def __init__(self):
            pass
        
        def left_door(self, color):
            door = [[20, 450, 10, 100, color]]
            return door
            
        def right_door(self, color):
            door = [[1890, 450, 10, 100, color]]
            return door
            
        def top_door(self, color):
            door = [[900, 20, 100, 10, color]]
            return door
            
        def bottom_door(self, color):
            door = [[900, 1050, 100, 10, color]]
            return door
            
              
class RoomBorders():
    def __init__(self):
        pass
        
    def left_right_door(self, color):
         
                       # Left-top
        border_list = [[0, 0, 30, 450, color],
                       # Left-bottom
                       [0, 550, 30, dY, color],
                       # Bottom
                       [0, 1050, dX, 30, color],
                       # Right-top
                       [1890, 0, 30, 450, color],
                       # Right-bottom
                       [1890, 550, 30, dY, color],
                       # Top
                       [0, 0, dX, 30, color]
                      ]
        return border_list
        
    def up_down_door(self, color):
        
                        # Top-left
        border_list = [[0, 0, 900, 30, color],
                        # Top-right
                       [1000, 0, 920, 30, color],
                        # Bottom-left
                       [0, 1050, 900, 30, color],
                        # Bottom-right
                       [1000, 1050, 920, 30, color],
                        # Left
                       [0, 0, 30, dY, color],
                        # Right
                       [1890, 0, 30, dY, color]
                      ]
        return border_list
        
    def left_up_door(self, color):
        
                        # Top-left
        border_list = [[0, 0, 900, 30, color],
                        # Top-right
                       [1000, 0, 920, 30, color],
                        # Bottom
                       [0, 1050, dX, 30, color],
                        # Right
                       [1890, 0, 30, dY, color],
                        # Left-top
                       [0, 0, 30, 450, color],
                        # Left-bottom
                       [0, 550, 30, dY, color]
                      ]
        return border_list
        
    def left_down_door(self, color):
        
                        # Top
        border_list = [[0, 0, dX, 30, color],
                        # Right
                       [1890, 0, 30, dY, color],
                        # Bottom-right
                       [1000, 1050, 920, 30, color],
                        # Bottom-left
                       [0, 1050, 900, 30, color],
                        # Left-bottom
                       [0, 550, 30, dY, color],
                        # Left-top
                       [0, 0, 30, 450, color]
                      ]
        return border_list       

    def right_down_door(self, color):
        
                        # Top        
        border_list = [[0, 0, dX, 30, color],
                        # Right-top
                       [1890, 0, 30, 450, color],
                        # Right-bottom
                       [1890, 550, 30, dY, color],
                        # Bottom-right
                       [1000, 1050, 920, 30, color],
                        # Bottom-left
                       [0, 1050, 900, 30, color],
                        # Left
                       [0, 0, 30, dY, color]
                      ]
        return border_list
        
    def right_up_door(self, color):
        
                        # Top-left       
        border_list = [[0, 0, 900, 30, color],
                        # Top-right
                       [1000, 0, 920, 30, color],
                        # Right-top
                       [1890, 0, 30, 450, color],
                        # Right-bottom
                       [1890, 550, 30, dY, color],
                        # Bottom
                       [0, 1050, dX, 30, color],
                        # Left
                       [0, 0, 30, dY, color]
                      ]
        return border_list
        
        
class Teleporter(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, 1900)
        self.rect.y = random.randrange(50, 1000)
        

    def teleporter_random_chance(self):
        random_num = random.randrange(20)
        if random_num == 1:
            return True
            
    def teleporter_collision_check(self, teleporter, objects):
        return pygame.sprite.groupcollide(teleporter, objects, True, False)
        
    def grid(self, dx, dy):
        """ Used to check to see if teleporter is spawned in front of cerain areas """
        grid = []
        for y in range(200):
            for x in range(200):
                grid.append([dx+x, dy+y])
        return grid
          
class Enemies(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1, 1900)
        self.rect.y = random.randint(1, 1000)
        self.health = 100
        self.room = None
        self.damage = 10
        self.speed = 5
        self.player = player
        
    def move_towards_player(self):
        vx = self.player.rect.x - self.rect.x
        vy = self.player.rect.y - self.rect.y
        dist = math.sqrt(vx**2 + vy**2)
        vx = vx / dist
        vy = vy / dist    
        return [vx, vy]
        
        
    def update(self):
        if self.health <= 0:
            self.kill()
        elif self.health > 0:
            self.rect.x += int(self.move_towards_player()[0] * self.speed)
            self.rect.y += int(self.move_towards_player()[1] * self.speed)
        
        
class En1(Enemies):
    def __init__(self, player):
        super().__init__(player)
        self.image.fill(CYAN)
        
class En2(Enemies):
    def __init__(self, player):
        super().__init__(player)
        self.image.fill(MIDNIGHTBLUE)
        

class Room():
    def __init__(self, player):
        self.player = player
        self.power_up_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.teleporter_list = pygame.sprite.Group()
        self.teleporter = Teleporter(WHITE)
        self.teleporter_xy = []
        self.borders = RoomBorders()
        self.doors = RoomDoors()
        if self.teleporter.teleporter_random_chance():
            self.teleporter_list.add(self.teleporter)
            self.teleporter_xy = [self.teleporter.rect.x, self.teleporter.rect.y]
            
        self.power_ups = []
        self.powerup = DamageUp(self.player)
        self.power_ups.append(self.powerup)
        self.powerup = SpeedUp(self.player)
        self.power_ups.append(self.powerup)
        
        if self.powerup.rand_chance():  
            rand_int = random.randrange(len(self.power_ups))
            self.power_up_list.add(self.power_ups[rand_int])
        
        
            
class Room_0(Room):
    def __init__(self, player):
        super().__init__(player)
        
        self.enemy = RandomEnemies(self.player).enemies_in_room
        for i in self.enemy:
            en = i
            self.enemy_list.add(en)
        
        
        walls = [[300, 200, 50, 350, RED],
                 [250, 600, 450, 50, RED],
                 [650, 350, 50, 350, RED],
                 [650, 350, 350, 50, RED],
                 [900, 200, 50, 450, RED],
                 [1500, 150, 50, 250, RED],
                 [1200, 800, 500, 50, RED]
                ]
                
        # Doors 
        for i in self.doors.left_door(RED):
            self.door1 = Wall(i[0], i[1], i[2], i[3], i[4])
            self.wall_list.add(self.door1)
        for i in self.doors.right_door(RED):
            self.door2 = Wall(i[0], i[1], i[2], i[3], i[4])
            self.wall_list.add(self.door2)
            
        # Borders
        for item in self.borders.left_right_door(BLUE):
            border = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(border)
            
        # Walls
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        # Teleporter
        if self.teleporter_xy in self.teleporter.grid(0, 350):
            self.teleporter.kill()
        elif self.teleporter_xy in self.teleporter.grid(1750, 350):
            self.teleporter.kill()
        self.teleporter.teleporter_collision_check(self.teleporter_list, self.wall_list)
        
        # Powerup
        self.powerup.collision_check(self.power_up_list, self.wall_list)
        
    def update(self):
        for i in self.enemy:
            i.update()
        for i in self.bullet_list:
            i.update()
        if len(self.enemy_list) <= 0:
            self.enemy_list.empty()
            self.door1.kill()
            self.door2.kill()
            
            
class Room_1(Room):
    def __init__(self, player):
        
        super().__init__(player)
        
        self.enemy = RandomEnemies(self.player).enemies_in_room
        for i in self.enemy:
            en = i
            self.enemy_list.add(en)

        walls = [[400, 300, 50, 200, PURPLE],
                 [350, 500, 50, 250, PURPLE],
                 [400, 750, 50, 200, PURPLE],
                 [550, 300, 50, 100, PURPLE],
                 [600, 350, 50, 200, PURPLE],
                 [650, 500, 150, 50, PURPLE],
                 [750, 550, 50, 400, PURPLE],
                 [900, 100, 250, 50, PURPLE],
                 [950, 400, 50, 250, PURPLE],
                 [1100, 150, 50, 250, PURPLE],
                 [1150, 350, 300, 50, PURPLE],
                 [1000, 600, 50, 150, PURPLE],
                 [1050, 700, 400, 50, PURPLE],
                 [1350, 600, 50, 100, PURPLE],
                 [1400, 150, 100, 50, PURPLE],
                 [1500, 200, 250, 50, PURPLE],
                 [1700, 250, 50, 50, PURPLE],
                 [1600, 400, 50, 200, PURPLE],
                 [1650, 550, 100, 50, PURPLE],
                 [1750, 300, 50, 300, PURPLE],
                 [1000, 800, 50, 100, PURPLE],
                 [1050, 850, 100, 50, PURPLE],
                 [1150, 900, 150, 50, PURPLE],
                 [1300, 850, 200, 50, PURPLE],
                 [1500, 900, 150, 50, PURPLE]
                ]
                
        # Doors
        for i in self.doors.left_door(RED):
            self.door1 = Wall(i[0], i[1], i[2], i[3], i[4])
            self.wall_list.add(self.door1)
        for i in self.doors.right_door(RED):
            self.door2 = Wall(i[0], i[1], i[2], i[3], i[4])
            self.wall_list.add(self.door2)
            
        # Borders        
        for item in self.borders.left_right_door(BLUE):
            border = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(border)
            
        # Walls   
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        # Teleporter    
        if self.teleporter_xy in self.teleporter.grid(0, 350):
            self.teleporter.kill()
        elif self.teleporter_xy in self.teleporter.grid(1750, 350):
            self.teleporter.kill()
        self.teleporter.teleporter_collision_check(self.teleporter_list, self.wall_list)
        
        # Powerup
        self.powerup.collision_check(self.power_up_list, self.wall_list)
        
    def update(self):
        for i in self.enemy:
            i.update()
        
        for i in self.bullet_list:
            i.update()
            
        if len(self.enemy_list) <= 0:
            self.enemy_list.empty()
            self.door1.kill()
            self.door2.kill()
            
class RandomEnemies():
        def __init__(self, player):
            self.enemy_list = [En1(player), En2(player), En1(player)]
            self.enemies_in_room = self.pick_enemies()
            
            for i in self.enemies_in_room:
                self.health = i.health
                
                
        def pick_enemies(self):
            rnd = random.randint(0, len(self.enemy_list))
            return random.sample(self.enemy_list, rnd)
            
        def update(self):
            for i in self.enemies_in_room:
                i.update()
        
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(50, 1900)
        self.rect.y = random.randrange(50, 1000)
        self.player = player
        
    def rand_chance(self):
        rand_int = random.randrange(50)
        if rand_int == 1:
            return True
        
    def collision_check(self, powerup, objects):
        return pygame.sprite.groupcollide(powerup, objects, True, False)
        
        
class DamageUp(PowerUp):
    def __init__(self, player):
        super().__init__(player)
        self.dmg = 5
        
    def pickup(self):
        self.player.damage += self.dmg
        
        
class SpeedUp(PowerUp):
    def __init__(self, player):
        super().__init__(player)
        self.speed = 4
        self.image.fill(TEAL)
        
    def pickup(self):
        self.player.speed += self.speed
        
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = dX / 2
        self.rect.y = dY / 2
        self.moveX = 0
        self.moveY = 0
        self.health = 100
        self.room = None
        self.health_timer = 0
        self.health_cooldown = 400
        self.damage = 10
        self.speed = 6
        self.shot_timer = 0
        self.shot_cooldown = 100
        self.is_shooting = False
        
    def enemy_collision_x(self, direction):
        enemy_hit_list = pygame.sprite.spritecollide(self, self.room.enemy_list, False)
        for enemy in enemy_hit_list:
            if direction > 0:
                self.rect.right = enemy.rect.left
            else:
                self.rect.left = enemy.rect.right
            if self.health_timer > self.health_cooldown:
                self.health -= enemy.damage
                self.health_timer = 0
                
    def enemy_collision_y(self, direction):
        enemy_hit_list = pygame.sprite.spritecollide(self, self.room.enemy_list, False)
        for enemy in enemy_hit_list:
            if direction > 0:
                self.rect.bottom = enemy.rect.top
            else:
                self.rect.top = enemy.rect.bottom
            if self.health_timer > self.health_cooldown:
                self.health -= enemy.damage
                self.health_timer = 0
                
    def power_up_collision(self):
        collision_list = pygame.sprite.spritecollide(self, self.room.power_up_list, True)
        for i in collision_list:
            i.pickup()
                
    def update(self):
        self.rect.x += self.moveX
        self.enemy_collision_x(self.moveX)
        teleporter_hit = pygame.sprite.spritecollide(self, self.room.teleporter_list, False)
        for item in teleporter_hit:
            self.rect.x = random.randrange(100, 1800)
            self.rect.y = random.randrange(100, 900)
        wall_hit_list = pygame.sprite.spritecollide(self, self.room.wall_list, False)
        for wall in wall_hit_list:
            if self.moveX > 0:
                self.rect.right = wall.rect.left
            else:
                self.rect.left = wall.rect.right

        self.rect.y += self.moveY
        self.enemy_collision_y(self.moveY)
        teleporter_hit = pygame.sprite.spritecollide(self, self.room.teleporter_list, False)
        for item in teleporter_hit:
            self.rect.x = random.randrange(100, 1800)
            self.rect.y = random.randrange(100, 900)
        wall_hit_list = pygame.sprite.spritecollide(self, self.room.wall_list, False)
        for wall in wall_hit_list:
            if self.moveY > 0:
                self.rect.bottom = wall.rect.top
            else:
                self.rect.top = wall.rect.bottom
                
        self.power_up_collision()
        
    def move_left(self):
        self.moveX = -self.speed
        
    def move_right(self):
        self.moveX = self.speed
        
    def move_up(self):
        self.moveY = -self.speed
        
    def move_down(self):
        self.moveY = self.speed
        
    def stopX(self):
        self.moveX = 0
        
    def stopY(self):
        self.moveY = 0
        
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, dest_x, dest_y):
        super().__init__()
        self.image = pygame.Surface([3, 3])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.floating_point_x = start_x
        self.floating_point_y = start_y
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff);
        self.velocity = 10
        self.moveX = math.cos(angle) * self.velocity
        self.moveY = math.sin(angle) * self.velocity
        self.player = None


        
    def update(self):
        self.floating_point_x += self.moveX
        self.floating_point_y += self.moveY
        self.rect.x = int(self.floating_point_x)
        self.rect.y = int(self.floating_point_y)
        
        if self.rect.x < 0 or self.rect.x > dX or self.rect.y < 0 or self.rect.y > dY:
            self.kill()
        bullet_wall_collision = pygame.sprite.spritecollide(self, self.room.wall_list, False)
        for bullet in bullet_wall_collision:
            self.kill()
        enemy_collision = pygame.sprite.spritecollide(self, self.room.enemy_list, False)
        for i in enemy_collision:
            self.room.enemy[self.room.enemy.index(i)].health -= self.player.damage
            
            self.kill()
            
   
def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode((dX, dY))
    clock = pygame.time.Clock()
    
    player = Player()   
    room_list = []
    room = Room_0(player)
    room_list.append(room)
    room = Room_1(player)
    room_list.append(room)
   
    current_room_no = 0
    current_room = room_list[current_room_no]

    all_sprite_list = pygame.sprite.Group()
    all_sprite_list.add(player)
    player.room = current_room

    while True:

        clock.tick(FPS)
        player.health_timer += clock.get_time()
        player.shot_timer += clock.get_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.move_left()
                if event.key == pygame.K_d:
                    player.move_right()
                if event.key == pygame.K_w:
                    player.move_up()
                if event.key == pygame.K_s:
                    player.move_down()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.moveX < 0:
                    player.stopX()
                if event.key == pygame.K_d and player.moveX > 0:
                    player.stopX()
                if event.key == pygame.K_w and player.moveY < 0:
                    player.stopY()
                if event.key == pygame.K_s and player.moveY > 0:
                    player.stopY()
                    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                player.is_shooting = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                player.is_shooting = False
    
        if player.is_shooting and player.shot_timer >= player.shot_cooldown:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            bullet = Bullet(player.rect.x + 10, player.rect.y + 10, mouse_x, mouse_y)
            bullet.room = player.room
            bullet.player = player
            bullet.room.bullet_list.add(bullet)
            player.shot_timer = 0
            
        # Room change   
        if player.rect.x >= dX:
            if current_room_no == 0:
                current_room_no = 1
                current_room = room_list[current_room_no]
                player.rect.x = 30
                player.room = current_room
        if player.rect.x <= -15:
            if current_room_no == 1:
                current_room_no = 0
                current_room = room_list[current_room_no]
                player.rect.x = dX
                player.room = current_room
        

        
        all_sprite_list.update()
        player.room.update()

        
        
       
        gameDisplay.fill(BLACK)
        current_room.power_up_list.draw(gameDisplay)
        current_room.bullet_list.draw(gameDisplay)
        current_room.enemy_list.draw(gameDisplay)
        current_room.wall_list.draw(gameDisplay)
        current_room.teleporter_list.draw(gameDisplay)
        all_sprite_list.draw(gameDisplay)
        pygame.display.update()
        
    pygame.quit()
    sys.exit
 
if __name__ == "__main__":
    main()