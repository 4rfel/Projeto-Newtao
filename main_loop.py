from pygame.locals import *
from ClasseNewton import *
import pygame
import os
import sys

Htela = 600
Ltela = 800
FPS = 30

white = (255,255,255)
pygame.init()

tela = pygame.display.set_mode((Ltela,Htela))
pygame.display.set_caption("JOGO NO NEWTON")
clock = pygame.time.Clock()
vidas = 3

newton = Newton('newton.png',(100),(390))
newton_group = pygame.sprite.Group()
newton_group.add(newton)
newton_maxJump = 20
maxJump = newton_maxJump

background = pygame.image.load(os.path.join("images","background.png")).convert()
bgX = 0
bgX2 = background.get_width()



def redrawWindow():
    tela.blit(background, (bgX,0))
    tela.blit(background, (bgX2,0))
    pygame.display.update()

    
speed = 30

            
while vidas >= 0:
    
    redrawWindow()
    clock.tick(speed)
    bgX -= 1.4
    bgX2 -= 1.4
    if bgX < background.get_width() * -1:
        bgX = background.get_width()
    if bgX2 < background.get_width() * -1:
        bgX2 = background.get_width()

    clock.tick(FPS)

    for event in pygame.event.get():
    #exit
        if event.type == pygame.QUIT:
            vidas = -1
    #Newton's movement
    if newton.jumping:
            newton.rect.y -= newton_maxJump
            newton_maxJump -= 1
            if newton_maxJump == 0:
                newton.falling = True
                newton.jumping = False
                newton_maxJump = maxJump
    newton.do()








    tela.blit(background, [0,0])
    newton_group.draw(tela)
    pygame.display.update()

pygame.display.quit()
