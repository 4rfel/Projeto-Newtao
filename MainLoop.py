import pygame
from ClasseNewton import Newton
from Heart import Heart
from Apple import Normal_apple, Rotten_apple, Life_apple
import json

with open('highscore.json', 'r') as h:
    highscore = int(json.loads(h.read()))
    
#highscore = 0
Htela = 600
Ltela = 800
FPS = 30

def Score(pontuacao):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Maças coletadas: " + str(pontuacao), True, black)
    tela.blit(text,(0,10))
    
def HighScore(pontuacao):
    font = pygame.font.SysFont(None, 25)
    text = font.render("HighScore: " + str(pontuacao), True, red)
    tela.blit(text,(0,30))

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
pygame.init()

tela = pygame.display.set_mode((Ltela,Htela))
pygame.display.set_caption("JOGO NO NEWTON")
clock = pygame.time.Clock()
vidas = 3
pontuacao = 0

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


#''' REMOVER ESSA PARTE DEPOIS OU USALA PARA TESTAR O PROGRAMA

vel_y_maca_boa = 5
vel_y_maca_ruim = 0
vel_y_life_apple = 4
vel_y_maca_ruim2 = 0

life_apple = Life_apple('heart-32X32.png', 200, 0, vel_y_life_apple)
normal_apple = Normal_apple('apple-28X33.png', 300, 0, vel_y_maca_boa)
rotten_apple = Rotten_apple('rotten_apple-33X49.png',(500),(500), vel_y_maca_ruim)
rotten_apple1 = Rotten_apple('rotten_apple-33X49.png',(400),(500), vel_y_maca_ruim2)
rotten_apple2 = Rotten_apple('rotten_apple-33X49.png',(600),(500), vel_y_maca_ruim2)

apple_group = pygame.sprite.Group()
apple_group.add(normal_apple)

rotten_apple_group = pygame.sprite.Group()
rotten_apple_group.add(rotten_apple1)
rotten_apple_group.add(rotten_apple)
rotten_apple_group.add(rotten_apple2)



life_apple_group = pygame.sprite.Group()
life_apple_group.add(life_apple)
#'''

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
        
    #gain lifes
    colisions = pygame.sprite.spritecollide(newton, life_apple_group, True)
    for e in colisions:
        if vidas == 1:
            heart_group.add(vidas2)
        if vidas == 2:
            heart_group.add(vidas3)
        if vidas == 3:
            vidas -= 1
            pontuacao += 10
        vidas += 1

    #Newton's movement
    if newton.jumping and not newton.falling:
            newton.rect.y -= newton_maxJump
#            if key[pygame.K_SPACE]:
#                newton_maxJump -= 1
            newton_maxJump -= 1
            if newton_maxJump == 0:
                newton.falling = True
                newton.jumping = False
                newton_maxJump = maxJump

    newton.do()
    normal_apple.cair()
    rotten_apple.cair()
    life_apple.cair()
    rotten_apple1.cair()
    
    tela.fill(white)
    Score(pontuacao)
    HighScore(highscore)
    newton_group.draw(tela)
    heart_group.draw(tela)
    apple_group.draw(tela)
    rotten_apple_group.draw(tela)
    life_apple_group.draw(tela)
    pygame.display.update()

if pontuacao > highscore:
    original = json.dumps(str(pontuacao), sort_keys = True, indent = 4)
else:
    original = str(highscore)
    
with open('highscore.json','w') as highscore:
    highscore.write(original)
pygame.display.quit()