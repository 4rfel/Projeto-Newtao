import pygame
from ClasseNewton import Newton
from Heart import Heart
from Apple import Apple
from Rotten_apple import Rotten_apple
from Falling_heart import Falling_heart
from GoldenApple import Golden_apple
from random import randrange
import json

with open('highscore.json', 'r') as h:
    highscore = int(json.loads(h.read()))

#highscore = 0
Htela = 500
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
timer = 0



#Newton
newton = Newton('newton1.png',(600),(550))
newton_group = pygame.sprite.Group()
newton_group.add(newton)
newton_maxJump = 18
maxJump = newton_maxJump

#Heart
vidas3 = Heart('heart-32X32.png',660,50)
vidas2 = Heart('heart-32X32.png',700,50)
vidas1 = Heart('heart-32X32.png',740,50)
heart_group = pygame.sprite.Group()
heart_group.add(vidas3)
heart_group.add(vidas2)
heart_group.add(vidas1)

rotten_apple_group = pygame.sprite.Group()
falling_heart_group = pygame.sprite.Group()
apple_group = pygame.sprite.Group()
golden_apple_group = pygame.sprite.Group()

normal = 0
rotten = 0
falling = 0

key = pygame.key.get_pressed()

fundo = pygame.image.load("background.png")

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
     # parte para ativar o caimento dos objetos
    timer += 1 
    if timer == 30:
        aleatorio = randrange(1,1000)
        if aleatorio <= 700:
            apple = Apple('apple.png', randrange(1,Ltela-100), -20, randrange(1,5))
            apple_group.add(apple)
            
        elif aleatorio >= 701 and aleatorio <= 949:
            #ativa rotten_apple
            rotten_apple = Rotten_apple('rotten_apple-33X49.png', randrange(1,Ltela-100), -20, randrange(1,5))
            rotten_apple_group.add(rotten_apple)
            
        elif aleatorio >= 950 and aleatorio <= 999:
            #ativa falling_heart
            falling_heart = Falling_heart('heart-32X32.png', randrange(1,Ltela-100), -20, randrange(1,5))
            falling_heart_group.add(falling_heart)
            
        if aleatorio == 1000:
            golden_apple = Golden_apple('golden_apple.png', randrange(1,Ltela-100), -20, 5)
            golden_apple_group.add(golden_apple)
            
        timer = 0
    
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
        
    colisions = pygame.sprite.spritecollide(newton, golden_apple_group, True)
    for e in colisions:
        pontuacao += 500
        
    #gain lifes
    colisions = pygame.sprite.spritecollide(newton, falling_heart_group, True)
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
            newton_maxJump -= 1
            if newton_maxJump == -maxJump:
                newton.falling = True
                newton.jumping = False
                newton_maxJump = maxJump

    newton.do()
    try:
        for apple in apple_group:
            apple.cair()
    except:''
    try:
        for rotten_apple in rotten_apple_group:
            rotten_apple.cair()
    except:''
    try:
        for falling_heart in falling_heart_group:
            falling_heart.cair()
    except:''
    try:
        for golden_apple in golden_apple_group:
            golden_apple.cair()
    except:''
    
    tela.blit(fundo, (0,0))
    Score(pontuacao)
    HighScore(highscore)
    newton_group.draw(tela)
    golden_apple_group.draw(tela)
    heart_group.draw(tela)
    apple_group.draw(tela)
    rotten_apple_group.draw(tela)
    falling_heart_group.draw(tela)
    pygame.display.update()

if pontuacao > highscore:
    original = json.dumps(str(pontuacao), sort_keys = True, indent = 4)
else:
    original = str(highscore)
    
with open('highscore.json','w') as highscore:
    highscore.write(original)
pygame.display.quit()