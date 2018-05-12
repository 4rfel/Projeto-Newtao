import pygame
from ClasseNewton import Newton
from Heart import Heart
from Apple import Apple
from Rotten_apple import Rotten_apple
from Falling_heart import Falling_heart
from GoldenApple import Golden_apple
from random import randrange
from background import Background
import json
from Chaos import Chao_continuo
from Buraco import Buraco
from Power_apple import Power_apple
from Power_bar import Power_bar


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
    
def HighScore(highscore):
    font = pygame.font.SysFont(None, 25)
    text = font.render("HighScore: " + str(highscore), True, red)
    tela.blit(text,(0,30))

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

pygame.init()
sem_controle = False
try:
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    
except:
    sem_controle = True

tela = pygame.display.set_mode((Ltela,Htela))
pygame.display.set_caption("JOGO NO NEWTON")
clock = pygame.time.Clock()
vidas = 3
pontuacao = 0
timer = 0


#  Fundo
vel_back = 3
background1 = Background("Fundos\\background.png",0,0,vel_back)
background2 = Background("Fundos\\background.png",800,0,vel_back)
background_group = pygame.sprite.Group()
background_group.add(background1)
background_group.add(background2)


# Chao
chao_inteiro = Chao_continuo('Fundos\\chao_inteiro.png',0,429,vel_back)
chao_inteiro2 = Chao_continuo('Fundos\\chao_inteiro.png',800,429,vel_back)
chao_group = pygame.sprite.Group()
chao_group.add(chao_inteiro)
chao_group.add(chao_inteiro2)


buraco = Buraco('Fundos\\buraco.png', -500, 429, vel_back)
lateral_buraco = Buraco('Fundos\\lateral.png', -500, 429, vel_back)
buraco_group = pygame.sprite.Group()
buraco_group.add(buraco)
lateral_group = pygame.sprite.Group()
lateral_group.add(lateral_buraco)


#Heart
vidas3 = Heart('Apples\\heart-32X32.png',660,50)
vidas2 = Heart('Apples\\heart-32X32.png',700,50)
vidas1 = Heart('Apples\\heart-32X32.png',740,50)
heart_group = pygame.sprite.Group()
heart_group.add(vidas3)
heart_group.add(vidas2)
heart_group.add(vidas1)


#Newton
newton = Newton(0,350)
newton_group = pygame.sprite.Group()
newton_group.add(newton)
newton_maxJump = 18
maxJump = newton_maxJump


# Power bar
power_bar = Power_bar(20,450)
power_bar_group = pygame.sprite.Group()
power_bar_group.add(power_bar)


# Apples
rotten_apple_group = pygame.sprite.Group()
falling_heart_group = pygame.sprite.Group()
apple_group = pygame.sprite.Group()
golden_apple_group = pygame.sprite.Group()
power_apple_group = pygame.sprite.Group()


dificuldade = 5
timer_dificuldade = 0
timer_chao = 0
troca_chao = True
morrer = 0
timer_buraco = 0
timer_poder = 0
apples_to_power = 6
poder_ativado = False
drop_interval = FPS
power_cd = 0



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
            if sem_controle:
                if event.key == pygame.K_SPACE and power_cd == apples_to_power and poder_ativado == False :
                    if not poder_ativado:
                        power_cd = 0
                    power_bar.power = 0
                    poder_ativado = True
        if not sem_controle:
            r2 = joystick.get_button(7)
            if r2 and power_cd == apples_to_power and poder_ativado == False:
                if not poder_ativado:
                        power_cd = 0
                power_bar.power = 0
                poder_ativado = True
                
     # parte para ativar o caimento dos objetos
    if not poder_ativado:
        timer += 1 
        if timer == drop_interval:
            aleatorio = randrange(1,100)
            if aleatorio <= 64:
                apple = Apple('Apples\\apple.png', randrange(1,Ltela-100), -20, randrange(1,dificuldade))
                apple_group.add(apple)
            
            if aleatorio >= 65 and aleatorio <= 69:
                power_apple = Power_apple('Apples\\blue_apple.png',randrange(1,Ltela-100), -20, 3)
                power_apple_group.add(power_apple)
                
            elif aleatorio >= 70 and aleatorio <= 89:
                #ativa rotten_apple
                rotten_apple = Rotten_apple('Apples\\rotten_apple-33X49.png', randrange(1,Ltela-100), -20, randrange(1,dificuldade))
                rotten_apple_group.add(rotten_apple)
                
            elif aleatorio >= 90 and aleatorio <= 99 :
                #ativa falling_heart
                falling_heart = Falling_heart('Apples\\heart-32X32.png', randrange(1,Ltela-100), -20, randrange(1,dificuldade))
                falling_heart_group.add(falling_heart)
                
            if aleatorio == 100:
                golden_apple = Golden_apple('Apples\\golden_apple.png', randrange(1,Ltela-100), -20, 5)
                golden_apple_group.add(golden_apple)
                
            timer = 0  
    
    timer_dificuldade += 1
    if timer_dificuldade == 20*FPS:
        if dificuldade <= 60:
            dificuldade += 1
        if dificuldade > 60:
            drop_interval -= 1
        timer_dificuldade = 0
    
    
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
    
    colisions = pygame.sprite.spritecollide(newton, buraco_group, False)
    for e in colisions:
        newton.morrendo = True
        newton.rect.y += morrer
        morrer += 1
        newton.rect.x -= vel_back
        if morrer >= 15:
            heart_group.remove(vidas1)
            heart_group.remove(vidas2)
            heart_group.remove(vidas3)
            vidas = -1
    
    colisions = pygame.sprite.spritecollide(newton, apple_group, True)
    for e in colisions:
        pontuacao += 1
    
    colisions = pygame.sprite.spritecollide(newton, power_apple_group, True)
    for e in colisions:
        if power_bar.power < apples_to_power:
            power_bar.power += 1
            power_cd += 1
        pontuacao += 5
        
    colisions = pygame.sprite.spritecollide(newton, golden_apple_group, True)
    for e in colisions:
        pontuacao += 150
        
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
    if newton.jumping and not newton.morrendo:
            newton.rect.y -= newton_maxJump
            newton_maxJump -= 1
            if newton_maxJump < -maxJump:
                newton.jumping = False
                newton_maxJump = maxJump
    
    newton.do()
    background1.lateral()
    background2.lateral()
    chao_inteiro.lateral()
    chao_inteiro2.lateral()
    buraco.lateral()
    lateral_buraco.lateral()
    power_bar.update()
    
    if not poder_ativado:
        try:
            for apple in apple_group:
                apple.cair()
                if apple.rect.y >= Htela:
                    pontuacao -= 1
                    apple_group.remove(apple)
        except:''
        try:
            for rotten_apple in rotten_apple_group:
                rotten_apple.cair()
        except:''
        try:
            for falling_heart in falling_heart_group:
                falling_heart.cair()
                if falling_heart.rect.y >= Htela:
                    rotten_apple_group.remove(rotten_apple)
        except:''
        try:
            for golden_apple in golden_apple_group:
                golden_apple.cair()
                if golden_apple.rect.y >= Htela:
                    golden_apple_group.remove(golden_apple)
        except:''
        try:
            for power_apple in power_apple_group:
                power_apple.cair()
                if power_apple < Htela:
                    power_apple_group.remove(power_apple)
        except:''
    
    if poder_ativado:
        timer_poder += 1
        if timer_poder == FPS*5:
            poder_ativado = False
            timer_poder = 0
        
    timer_chao += 1
    if timer_chao == FPS*9:
        if troca_chao:
            chao_inteiro.rect.x = 800
            troca_chao = False
        else:
            chao_inteiro2.rect.x = 800
            troca_chao = True
        timer_chao = 0
        
    timer_buraco += 1
    if timer_buraco == FPS*11:
        aleatorio = randrange(1,4)
        if aleatorio >= 1:
            buraco.rect.x = 900
            lateral_buraco.rect.x = 800
        timer_buraco = 0
    
    tela.fill(white)
    chao_group.draw(tela)
    background_group.draw(tela)
    lateral_group.draw(tela)
    power_bar_group.draw(tela)
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

print(dificuldade)
print(drop_interval)

pygame.display.quit()