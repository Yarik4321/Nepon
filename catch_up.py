from pygame import *
import pygame
from random import randint 

pygame.init()
pygame.mixer.init()


kick = pygame.mixer.Sound("kick.ogg")

win = pygame.display.set_mode((700,500))
pygame.display.set_caption('Labirint')
bg = pygame.transform.scale(pygame.image.load('background.jpg'),(700,500))

class GameSprite():
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x 
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
        
class Hero(GameSprite):
    def update(self):
        if self.rect.y <= 250 and self.rect.x <= 635:
            self.direction = 'down'
        if self.rect.x >= 350 and self.rect.y >= 0:
            self.direction2 = "left"
        if self.rect.y >= 400 and self.rect.x >= 0:
            self.direction = "up"
        if self.rect.x <= 200 and self.rect.y <= 435:
            self.direction2 = "right"

        if self.direction2 == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed  
        if self.direction == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    direction1 = 'up'   
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 650:
            self.direction = "left"
        
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed




class Hero(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


class Wall():
    def __init__ (self,wall_x,wall_y,wall_width,wall_height):
        self.color_1 = randint(0,255)
        self.color_2 = randint(0,255)
        self.color_3 = randint(0,255)     
        self.width = wall_width
        self.height = wall_height
        self.wall_x = wall_x           
        self.wall_y = wall_y
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.image.fill((self.color_1,self.color_2,self.color_3))
    def draw_wall(self):
        win.blit(self.image,(self.wall_x,self.wall_y))



hero  = Hero('hero.png',50,100,5)
enemy = Enemy('cyborg.png',520,325,2)
enemy1 = Enemy('cyborg.png',520,150,3)
gold = GameSprite('treasure.png',590,420,0)

wl_1 = Wall(0,0,10,500)
wl_2 = Wall(690,0,10,500)
wl_3 = Wall(0,0,700,10)
wl_4 = Wall(0,490,700,10)
wl_5 = Wall(200,100,10,300)
wl_6 = Wall(490,100,10,300)
wl_7 = Wall(200,100,300,10)
wl_8 = Wall(200,390,300,10)

wl_1.draw_wall()

wl_2.draw_wall()
wl_3.draw_wall()
wl_4.draw_wall()
wl_5.draw_wall()
wl_6.draw_wall()
wl_7.draw_wall()
wl_8.draw_wall()





#window = display.set_mode((win_width, win_height))
#display.set_caption("Maze")
#background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#player = Player('hero.png', 5, win_height - 80, 4)
#monster = Enemy('cyborg.png', win_width - 80, 280, 2)
#final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

FPS = 60
clock = pygame.time.Clock()
game = True
while game:
    win.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if hero.rect.colliderect(enemy.rect) or hero.rect.colliderect(enemy1.rect):
            kik.play()
            hero.rect.x = 50
            hero.rect.y = 100 

    if hero.rect.colliderect(gold):
        exit()
          


    enemy.reset()
    enemy.update()
    hero.reset()
    hero.Update()
    gold.reset()
    enemy1.update_cube()
    enemy1.reset()

    wl_1 = Wall(0,0,10,500)
    wl_2 = Wall(690,0,10,500)
    wl_3 = Wall(0,0,700,10)
    wl_4 = Wall(0,490,700,10)
    wl_5 = Wall(200,100,10,300)
    wl_6 = Wall(490,100,10,300)
    wl_7 = Wall(200,100,300,10)
    wl_8 = Wall(200,390,300,10)

    wl_1.draw_wall()
    wl.draw_wall()
    wl_2.draw_wall()
    wl_3.draw_wall()
    wl_4.draw_wall()
    wl_5.draw_wall()
    wl_6.draw_wall()
    wl_7.draw_wall()
    wl_8.draw_wall()


    pygame.display.update()
    clock.tic(FPS)