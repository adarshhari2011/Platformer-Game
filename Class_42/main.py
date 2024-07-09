# Example file showing a circle moving on screen
import pygame
import random 
blue_tile=pygame.image.load("tiles/1.png")
brown_tile=pygame.image.load("tiles/2.png")
water_tile=pygame.image.load("tiles/3.png")
green_tile=pygame.image.load("tiles/4.png")
purple_tile=pygame.image.load("tiles/5.png")
yellow_tile=pygame.image.load("tiles/6.png")
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 900))
clock = pygame.time.Clock()
running = True
dt = 0
map = [ [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
        [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]]
 

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

x = 0
class Player:
    def __init__(self):   
     self.x = 0
     self.y = 0
     self.height = 10
     self.width = 10
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: 
            if self.y > 40 :
                self.y -= 10
            else : 
                level1Map.y_shift += 10
        if keys[pygame.K_s]:
            if self.y < 860 :
                self.y += 10
            else : 
                level1Map.y_shift -= 10
        if keys[pygame.K_a]:
            if self.x > 40 :
                self.x -= 10
            else : 
                level1Map.x_shift += 10
        if keys[pygame.K_d]:
            if self.x < 760 :
                self.x += 10
            else : 
                level1Map.x_shift -= 10
    def display(self):
        pygame.draw.circle(screen, "red", (self.x,self.y), 40)
class Block:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.height = 50
        self.width = 50

    def display(self,screen):
        print()
class BrownBlock(Block):
    def display(self, screen):
        screen.blit(brown_tile,[self.x , self.y , self.width , self.height])
class WaterBlock(Block):
    def display(self, screen):
        screen.blit(water_tile,[self.x , self.y , self.width , self.height])
class GrassBlock(Block):
    def display(self, screen):
        screen.blit(green_tile,[self.x , self.y , self.width , self.height])
class Map:
    def __init__(self) : 
        self.level = 1 
        self.map = map 
        self.x_shift = 0
        self.y_shift = 0
    def display(self,screen):
        length = 50
        for row in range(len(map)):
            for col in range(len(map[0])):
                if self.map[row][col] == 1 : 
                    block = Block(col*length+self.x_shift , row*length+ self.y_shift)
                    block.display(screen)
                elif self.map[row][col] == 2:
                    brownblock = BrownBlock(col*length+self.x_shift , row*length+ self.y_shift)  
                    brownblock.display(screen)
                elif self.map[row][col] == 3:
                    water_tile = WaterBlock(col*length+self.x_shift , row*length+ self.y_shift)  
                    water_tile.display(screen)
                elif self.map[row][col] == 4:
                    grassblook = GrassBlock(col*length+self.x_shift , row*length+ self.y_shift)  
                    grassblook.display(screen)


level1Map = Map()

player=Player()
framerate = 120
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("grey")
    level1Map.display(screen)

    player.movement()
    player.display()
    
    pygame.display.flip()
    dt = clock.tick(framerate) / 1000

pygame.quit()