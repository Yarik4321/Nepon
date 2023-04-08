import pygame , sys
from pygame.locals import *

pygame.init()
windowSurface = pygame.display.set_mode((1000,1000))

pygame.display.set_caption('Привет мир!')
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN =(0,255,0)
BLUE = (0,0,255)

basicFont = pygame.font.SysFont('Arial',100)

text = basicFont.render('Привет мир!', True,WHITE,BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface.fill(WHITE)

pygame.draw.polygon(windowSurface,GREEN,((146,0),(291,106),(236,277),(56, 277),(0,106)))

windowSurface.blit(text,textRect)

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()