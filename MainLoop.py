from ClasseNewton import *
import pygame
from Heart import *

Htela = 600
Ltela = 800
FPS = 30

white = (255,255,255)
pygame.init()

tela = pygame.display.set_mode((Ltela,Htela))
pygame.display.set_caption("JOGO NO NEWTON")
clock = pygame.time.Clock()
vidas = 3

#Newton
newton = Newton('newton-122X175.png',(100),(390))
newton_group = pygame.sprite.Group()
newton_group.add(newton)
newton_maxJump = 20
maxJump = newton_maxJump

#Heart
heart1 = Heart('heart-32X32.png',660,50)
heart2 = Heart('heart-32X32.png',700,50)
heart3 = Heart('heart-32X32.png',740,50)
heart_group = pygame.sprite.Group()
heart_group.add(heart1)
heart_group.add(heart2)
heart_group.add(heart3)


''' REMOVER ESSA PARTE DEPOIS OU USALA PARA TESTAR O PROGRAMA

class Apple(pygame.sprite.Sprite):
    def __init__(self, imagem, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
apple = Apple('heart-32X32.png',(500),(0))
apple_group = pygame.sprite.Group()
apple_group.add(apple)
'''

imunidade = FPS
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
    if pygame.sprite.collide_rect(apple, newton):
            if vidas == 1 and imunidade == FPS:
                imunidade -= 1
                apple.rect.y = -500
                apple_group.remove(apple)
                heart3.kill()
                vidas = 0
            if vidas == 2 and imunidade == FPS:
                imunidade -= 1
                apple.rect.y = -500
                heart2.kill()
                apple_group.remove(apple)
                vidas = 1
            if vidas == 3 and imunidade == FPS:
                imunidade -= 1
                apple.rect.y = -500
                heart1.kill()
                apple_group.remove(apple)
                vidas = 2
                
    #Imunidade
    if imunidade < FPS:
        imunidade -= 1
        if imunidade == 0:
            imunidade = FPS
    
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
    apple_group.draw(tela)
    pygame.display.update()

pygame.display.quit()