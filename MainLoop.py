import pygame
from ClasseNewton import Newton
from Heart import Heart
from Apple import Apple
from Rotten_apple import Rotten_apple
from Falling_heart import Falling_heart
from random import randrange

Htela = 600
Ltela = 800
FPS = 30

white = (255,255,255)
pygame.init()

tela = pygame.display.set_mode((Ltela,Htela))
pygame.display.set_caption("JOGO NO NEWTON")
clock = pygame.time.Clock()
vidas = 3
pontuacao = 0

# apple
apple = Apple('apple.png',(0),(200),(randrange(1,5)))
apple_group = pygame.sprite.Group()
apple_group.add(apple)

#rotten apple
Rotten_apple = Rotten_apple('rotten_apple-33X49.png',(0),(200),randrange(1,5))
rotten_apple_group = pygame.sprite.Group()
rotten_apple_group.add(Rotten_apple)


#Newton
newton = Newton('newton-122X175.png',(100),(390))
newton_group = pygame.sprite.Group()
newton_group.add(newton)
newton_maxJump = 20
maxJump = newton_maxJump

#Heart
vidas3 = Heart('heart-32X32.png',660,50)
vidas2 = Heart('heart-32X32.png',700,50)
vidas1 = Heart('heart-32X32.png',740,50)
heart_group = pygame.sprite.Group()
heart_group.add(vidas3)
heart_group.add(vidas2)
heart_group.add(vidas1)
#falling heart
falling_heart = Falling_heart('heart-32X32.png',(0),(200),randrange(1,5))
falling_heart_group = pygame.sprite.Group()
falling_heart_group.add(falling_heart)


key = pygame.key.get_pressed()

#Mainloop
while vidas > 0:

    clock.tick(FPS)

    for event in pygame.event.get():
    #exit
        if event.type == pygame.QUIT :
            vidas = -1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                vidas = -1
    # lose lifes
    colisions = pygame.sprite.spritecollide(newton, rotten_apple_group, True)
    for e in colisions:
        if vidas == 1:
            heart_group.remove(vidas1)
            vidas = 0
        if vidas == 2:
            heart_group.remove(vidas2)
            vidas = 1
        if vidas == 3:
            heart_group.remove(vidas3)
            vidas = 2
                
                
    colisions = pygame.sprite.spritecollide(newton, apple_group, True)
    for e in colisions:
        pontuacao += 1
#        score.marcouPonto = True
#        score.do()
    
    colisions = pygame.sprite.spritecollide(newton, falling_heart_group, True)
    for e in colisions:
        if vidas == 1:
            heart_group.add(vidas2)
        if vidas == 2:
            heart_group.add(vidas3)
        if vidas == 3:
            pontuacao += 10
        vidas += 1
    
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
    heart_group.draw(tela)
    pygame.display.update()

pygame.display.quit()
