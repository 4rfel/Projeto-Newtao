import ClasseNewton
import pygame

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

while vidas >= 0:

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


    tela.fill(white)
    newton_group.draw(tela)
    pygame.display.update()

pygame.display.quit()