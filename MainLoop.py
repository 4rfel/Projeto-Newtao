import pygame
from ClasseNewton import Newton
from Heart import Heart
from Apple import Apple
from Rotten_apple import Rotten_apple
from Falling_heart import Falling_heart
from GoldenApple import Golden_apple
from random import randrange
from background import Arvores
import json
from Chaos import Chao_continuo
from Buraco import Buraco
from Power_apple import Power_apple
from Power_bar import Power_bar
from Sky import Sky
from Mostrador import Mostrador
from Menu import Menu_imagens
from ClasseEinstein import Einstein
from ClasseHawking import Hawking
from firebase import firebase

firebase = firebase.FirebaseApplication('https://highscore-global.firebaseio.com/', None)
if firebase.get('highscore', None) is None:
    highscore = {}
else:
    highscore = firebase.get('highscore', None)

with open('highscore.json', 'r') as h:
    highscore = int(json.loads(h.read()))

#highscore = 0
Htela = 500
Ltela = 800



def Score(pontuacao):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Maças coletadas: " + str(int(pontuacao)), True, black)
    tela.blit(text,(0,10))


def HighScore(highscore):
    font = pygame.font.SysFont(None, 25)
    text = font.render("HighScore: " + str(highscore), True, red)
    tela.blit(text,(0,30))

def NewHighScore(highscore):
    font = pygame.font.SysFont(None, 30)
    text = font.render(" NEW HighScore: " + str(highscore), True, red)
    tela.blit(text,(0,35))

def Multiplicador(multiplicador):
    font = pygame.font.SysFont(None,40)
    text = font.render(str(multiplicador) + 'X', True, gold)
    tela.blit(text,(700,100))

black = (0,0,0)
red = (255,0,0)
gold = (218,165,32)

pygame.init()
pygame.mixer.init()
backgrond_sound = pygame.mixer.Sound('Sound_effects\\background_sound.ogg')
#backgrond_sound = pygame.mixer.Sound('Sound_effects\\aa.wav')
pygame.mixer.Sound.stop(backgrond_sound)


try:
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
except:''

tela = pygame.display.set_mode((Ltela,Htela))
pygame.display.set_caption("JOGO NO NEWTON")
clock = pygame.time.Clock()
vidas = 3
pontuacao = 0




#  Arvores
vel_arvores = 4

arvore1 = Arvores("Fundos\\background.png",0,0,vel_arvores)
arvore2 = Arvores("Fundos\\background.png",810,0,vel_arvores)
arvore_group = pygame.sprite.Group()
arvore_group.add(arvore1)
arvore_group.add(arvore2)


# Sky
vel_sky = 1

sky1 = Sky('Fundos\\sky.png',0,0,vel_sky)
sky2 = Sky('Fundos\\sky.png',800,0,vel_sky)
sky_group = pygame.sprite.Group()
sky_group.add(sky1)
sky_group.add(sky2)


# Chao
vel_chao = 5
timer_buraco = 0
timer_chao = 0
troca_chao = True
morrer = 0

chao_inteiro = Chao_continuo('Fundos\\grass.png',0,422,vel_chao)
chao_inteiro2 = Chao_continuo('Fundos\\grass.png',700,422,vel_chao)
chao_inteiro3 = Chao_continuo('Fundos\\grass.png',1200,422,vel_chao)
chao_group = pygame.sprite.Group()
chao_group.add(chao_inteiro)
chao_group.add(chao_inteiro2)
chao_group.add(chao_inteiro3)

buraco = Buraco('Fundos\\buraco.png', -500, 410, vel_chao)
buraco_group = pygame.sprite.Group()
buraco_group.add(buraco)

lateral_buraco = Buraco('Fundos\\lateral.png', -500, 425, vel_chao)
lateral_group = pygame.sprite.Group()
lateral_group.add(lateral_buraco)


#Heart
vidas3 = Heart('Apples\\heart.png',660,50)
vidas2 = Heart('Apples\\heart.png',700,50)
vidas1 = Heart('Apples\\heart.png',740,50)
heart_group = pygame.sprite.Group()
heart_group.add(vidas3)
heart_group.add(vidas2)
heart_group.add(vidas1)


#player
player_group = pygame.sprite.Group()


player_maxJump = 18
maxJump = player_maxJump


# Power bar
timer_poder = 0
power_cd = 0
apples_to_power = 5
poder_ativado = False

power_bar = Power_bar(20,450)
power_bar_group = pygame.sprite.Group()
power_bar_group.add(power_bar)


# Apples
rotten_apple_group = pygame.sprite.Group()
falling_heart_group = pygame.sprite.Group()
apple_group = pygame.sprite.Group()
golden_apple_group = pygame.sprite.Group()
power_apple_group = pygame.sprite.Group()


paused = False

#menu
menu  = Menu_imagens('Menus\\menu_atual-0.png',0,0)
menu_group = pygame.sprite.Group()
menu_group.add(menu)

FPS = 30

sem_controle = True
menu_rodando = True


multiplicador = 1

# menu
while menu_rodando:
    clock.tick(FPS)

    for event in pygame.event.get():
         if event.type == pygame.QUIT :
             menu  = False
             vidas = -1
         if event.type == pygame.KEYDOWN:
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE:
                     vidas = -1
                     menu_rodando = False
             if event.key == pygame.K_SPACE:
                 sem_controle = True
                 menu_rodando = False

                 #personagem = 'newton'
                 #personagem = 'einstein'
                 personagem = 'hawking'

                 if personagem == 'newton':
                     newton = Newton(200,340)
                     player_group.add(newton)
                     newton.sem_controle = True
                 if personagem == 'einstein':
                     einstein = Einstein(200,340)
                     player_group.add(einstein)
                     einstein.sem_controle = True
                 if personagem == 'hawking':
                     hawking = Hawking(200,340)
                     player_group.add(hawking)
                     hawking.sem_controle = True

    try:
        X = joystick.get_button(2)
        if X:

            sem_controle = False
            menu_rodando = False
            newton.sem_controle = False
#            personagem = 'newton'
#            personagem = 'einstein'
            personagem = 'hawking'

            if personagem == 'newton':
                 newton = Newton(200,340)
                 player_group.add(newton)
                 newton.sem_controle = False
            if personagem == 'einstein':
                einstein = Einstein(200,340)
                player_group.add(einstein)
                einstein.sem_controle = False
            if personagem == 'hawking':
                hawking = Hawking(200,340)
                player_group.add(hawking)
                hawking.sem_controle = False


    except:''


    menu_group.draw(tela)
    pygame.display.update()

if not sem_controle:
    personagem = 'newton'
    newton = Newton(200,340)
    player_group.add(newton)

    #personagem = 'hawking'
    #hawking = Hawking(200,340)
    #player_group.add(hawking)

    #personagem == 'einstein'
    #einstein = Einstein(200,340)
    #player_group.add(einstein)


#Mostrador da maças
some = 0
if sem_controle:
    mostrador = Mostrador('Fundos\\mostrador_teclado.png',(Ltela/2-100),(Htela/2-71))
if not sem_controle:
    mostrador = Mostrador('Fundos\\mostrador_controle.png',(Ltela/2-100),(Htela/2-71))
mostrador_group = pygame.sprite.Group()
mostrador_group.add(mostrador)


# Dificuldade
difuldade_timer = 0
dificuldade = 5
timer_dificuldade = 0
drop_interval = 30
miguezao = 0
elmigue = pygame.mixer.music.set_endevent()
FPS = 100
poder_ativado = False
#Mainloop
while vidas > 0:

    clock.tick(FPS)
    miguezao += 1
    if miguezao == 1:
        pygame.mixer.Sound.set_volume(backgrond_sound,0.3)
        pygame.mixer.Sound.play(backgrond_sound)
    for event in pygame.event.get():
    #exit
        if event.type == pygame.QUIT :
            vidas = -1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                vidas = -1
            if event.key == pygame.K_9:
                FPS = 100


            if sem_controle:
                if event.key == pygame.K_SPACE and power_cd == apples_to_power and poder_ativado == False:
                    if not poder_ativado:
                        power_cd = 0
                    power_bar.power = 0
                    poder_ativado = True

        if not sem_controle:
            R2 = joystick.get_button(7)
            if R2 and power_cd == apples_to_power and poder_ativado == False:
#                if not poder_ativado:
#                        power_cd = 0
                power_cd = 0
                power_bar.power = 0
                poder_ativado = True


    # poder especial
    if poder_ativado:
        timer_poder += 1
        if timer_poder == FPS*5:
            poder_ativado = False
            timer_poder = 0
            if personagem == 'einstein':
                FPS = 100
        if personagem == 'einstein':
            FPS = 60


     # spawn das maças
    if some >= FPS*5:
        difuldade_timer += 1
        if difuldade_timer == drop_interval:
            aleatorio = randrange(1,101)
            if aleatorio <= 50:
                apple = Apple('Apples\\apple.png', randrange(1,Ltela-100), -40, randrange(1,dificuldade))
                apple_group.add(apple)

            if aleatorio >= 51 and aleatorio <= 55:
                power_apple = Power_apple('Apples\\blue_apple.png',randrange(1,Ltela-100), -40, 3)
                power_apple_group.add(power_apple)

            if aleatorio >= 56 and aleatorio <= 89:
                if not poder_ativado and personagem == 'newton' or personagem != 'newton':
                    #ativa rotten_apple
                    rotten_apple = Rotten_apple('Apples\\rotten_apple.png', randrange(1,Ltela-100), -40, randrange(1,dificuldade))
                    rotten_apple_group.add(rotten_apple)

            if aleatorio >= 90 and aleatorio <= 99 :
                #ativa falling_heart
                falling_heart = Falling_heart('Apples\\heart.png', randrange(1,Ltela-100), -40, randrange(1,dificuldade))
                falling_heart_group.add(falling_heart)

            if aleatorio >= 100:
                golden_apple = Golden_apple('Apples\\golden_apple.png', randrange(1,Ltela-100), -40, 5)
                golden_apple_group.add(golden_apple)

            difuldade_timer = 0
    # aumento de dificuldade
    timer_dificuldade += 1
    if timer_dificuldade == 20*FPS:
        if dificuldade <= 60:
            dificuldade += 1
        if dificuldade > 60:
            if drop_interval > 0:
                drop_interval -= 1
        timer_dificuldade = 0


    # pegar maça podre
    try:
        if personagem == 'newton':
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

            #cair no buraco
            colisions = pygame.sprite.spritecollide(newton, buraco_group, False)
            for e in colisions:
                newton.morrendo = True
                newton.rect.y += morrer
                morrer += 1
                newton.rect.x -= vel_chao
                if morrer >= 15:
                    heart_group.remove(vidas1)
                    heart_group.remove(vidas2)
                    heart_group.remove(vidas3)
                    vidas = -1
            #coletar maças
            colisions = pygame.sprite.spritecollide(newton, apple_group, True)
            for e in colisions:
                pontuacao += 1 * multiplicador
                multiplicador += 0.01
            #pegar maça azul
            colisions = pygame.sprite.spritecollide(newton, power_apple_group, True)
            for e in colisions:
                if power_bar.power < apples_to_power:
                    power_bar.power += 1
                    power_cd += 1
                pontuacao += 5 * multiplicador
                multiplicador += 0.05
            # pegar maça de ouro
            colisions = pygame.sprite.spritecollide(newton, golden_apple_group, True)
            for e in colisions:
                pontuacao += 150 * multiplicador
                multiplicador += 0.5

            #pegar coraçoes
            colisions = pygame.sprite.spritecollide(newton, falling_heart_group, True)
            for e in colisions:
                if vidas == 1:
                    heart_group.add(vidas2)
                if vidas == 2:
                    heart_group.add(vidas3)
                if vidas == 3:
                    vidas -= 1
                    pontuacao += 10 * multiplicador
                    multiplicador += 0.03
                vidas += 1
    except:''

    try:
        if personagem == 'einstein':
            colisions = pygame.sprite.spritecollide(einstein, rotten_apple_group, True)
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

            #cair no buraco
            colisions = pygame.sprite.spritecollide(einstein, buraco_group, False)
            for e in colisions:
                newton.morrendo = True
                newton.rect.y += morrer
                morrer += 1
                newton.rect.x -= vel_chao
                if morrer >= 15:
                    heart_group.remove(vidas1)
                    heart_group.remove(vidas2)
                    heart_group.remove(vidas3)
                    vidas = -1
            #coletar maças
            colisions = pygame.sprite.spritecollide(einstein, apple_group, True)
            for e in colisions:
                pontuacao += 1 * multiplicador
                multiplicador += 0.01
            #pegar maça azul
            colisions = pygame.sprite.spritecollide(einstein, power_apple_group, True)
            for e in colisions:
                if power_bar.power < apples_to_power:
                    power_bar.power += 1
                    power_cd += 1
                pontuacao += 5 * multiplicador
                multiplicador += 0.05
            # pegar maça de ouro
            colisions = pygame.sprite.spritecollide(einstein, golden_apple_group, True)
            for e in colisions:
                pontuacao += 150 * multiplicador
                multiplicador += 0.5

            #pegar coraçoes
            colisions = pygame.sprite.spritecollide(einstein, falling_heart_group, True)
            for e in colisions:
                if vidas == 1:
                    heart_group.add(vidas2)
                if vidas == 2:
                    heart_group.add(vidas3)
                if vidas == 3:
                    vidas -= 1
                    pontuacao += 10 * multiplicador
                    multiplicador += 0.03
                vidas += 1
    except:''

    try:
        if personagem == 'hawking':
            colisions = pygame.sprite.spritecollide(hawking, rotten_apple_group, True)
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

            #cair no buraco
            colisions = pygame.sprite.spritecollide(hawking, buraco_group, False)
            for e in colisions:
                hawking.morrendo = True
                hawking.rect.y += morrer
                morrer += 1
                hawking.rect.x -= vel_chao
                if morrer >= 15:
                    heart_group.remove(vidas1)
                    heart_group.remove(vidas2)
                    heart_group.remove(vidas3)
                    vidas = -1
            #coletar maças
            colisions = pygame.sprite.spritecollide(hawking, apple_group, True)
            for e in colisions:
                pontuacao += 1 * multiplicador
                multiplicador += 0.01
            #pegar maça azul
            colisions = pygame.sprite.spritecollide(hawking, power_apple_group, True)
            for e in colisions:
                if power_bar.power < apples_to_power:
                    power_bar.power += 1
                    power_cd += 1
                pontuacao += 5 * multiplicador
                multiplicador += 0.05
            # pegar maça de ouro
            colisions = pygame.sprite.spritecollide(hawking, golden_apple_group, True)
            for e in colisions:
                pontuacao += 150 * multiplicador
                multiplicador += 0.5

            #pegar coraçoes
            colisions = pygame.sprite.spritecollide(hawking, falling_heart_group, True)
            for e in colisions:
                if vidas == 1:
                    heart_group.add(vidas2)
                if vidas == 2:
                    heart_group.add(vidas3)
                if vidas == 3:
                    vidas -= 1
                    pontuacao += 10 * multiplicador
                    multiplicador += 0.03
                vidas += 1
    except:''

    #newton
    try:
        if personagem == 'newton':
            newton.idle_walk()
            newton.do()
            if newton.jumping and not newton.morrendo:
                newton.rect.y -= player_maxJump
                player_maxJump -= 1
                if player_maxJump < -maxJump:
                    player_maxJump = maxJump
                    newton.jumping = False

    except:''
    #einstein
    try:
        if personagem == 'einstein':
            einstein.idle_walk()
            einstein.do()
            if einstein.jumping and not einstein.morrendo:
                einstein.rect.y -= player_maxJump
                player_maxJump -= 1
                if player_maxJump < -maxJump:
                    einstein.jumping = False
                    player_maxJump = maxJump
    except:''
    #hawking
    try:
        if personagem == 'hawking':
            hawking.idle_walk()
            hawking.do()
            if hawking.jumping and not hawking.morrendo:
                hawking.rect.y -= player_maxJump
                player_maxJump -= 1
                if player_maxJump < -maxJump:
                    hawking.jumping = False
                    player_maxJump = maxJump
    except:''
    #sky
    sky1.lateral()
    sky2.lateral()
    #arvore
    arvore1.lateral()
    arvore2.lateral()
    #chao
    chao_inteiro.lateral()
    chao_inteiro2.lateral()
    chao_inteiro3.lateral()
    buraco.lateral()
    lateral_buraco.lateral()
    #power bar
    power_bar.update()
    #apples

    some += 1
    if some >= 5*FPS:
        mostrador.rect.y += 3
        if mostrador.rect.y >= Htela:
            mostrador.kill()


    if some >= 5*FPS:
        try:
            for apple in apple_group:
                if personagem == 'hawking' and poder_ativado:
                    if apple.rect.x < Ltela/2:
                        apple.rect.x += 2
                    if apple.rect.x > Ltela/2:
                        apple.rect.x -= 2
                    if apple.rect.y > Ltela/2-270:
                        apple.rect.y -= 5

                apple.cair()
                if apple.rect.y >= Htela:
                    pontuacao -= 1
                    multiplicador = 1
                    apple_group.remove(apple)
        except:''
        try:
             if not poder_ativado and personagem == 'newton' or personagem != 'newton':
                for rotten_apple in rotten_apple_group:
                    rotten_apple.cair()
                    if rotten_apple.rect.y >= Htela:
                        multiplicador = 1
                        rotten_apple_group.remove(rotten_apple)
        except:''
        try:
            for falling_heart in falling_heart_group:
                if personagem == 'hawking' and poder_ativado:
                    if falling_heart.rect.x < Ltela/2:
                        falling_heart.rect.x += 2
                    if falling_heart.rect.x > Ltela/2:
                        falling_heart.rect.x -= 2
                    if falling_heart.rect.y > Ltela/2-270:
                        falling_heart.rect.y -= 5

                falling_heart.cair()
                if falling_heart.rect.y >= Htela:
                    multiplicador = 1
                    falling_heart_group.remove(falling_heart)
        except:''
        try:
            if not poder_ativado and personagem == 'newton':
                for golden_apple in golden_apple_group:
                    golden_apple.cair()
                    if golden_apple.rect.y >= Htela:
                        multiplicador = 1
                        golden_apple_group.remove(golden_apple)
            if personagem == 'hawking':
                if poder_ativado:
                    if golden_apple.rect.x < Ltela/2:
                        golden_apple.rect.x += 2
                    if golden_apple.rect.x > Ltela/2:
                        golden_apple.rect.x -= 2
                    if apple.rect.y > Ltela/2-270:
                        golden_apple.rect.y -= 5
                if golden_apple.rect.y >= Htela:
                    multiplicador = 1
                    golden_apple_group.remove(golden_apple)
        except:''
        try:
            for power_apple in power_apple_group:
                if personagem == 'hawking' and poder_ativado:
                    if power_apple.rect.x < Ltela/2:
                        power_apple.rect.x += 3
                    if apple.rect.x > Ltela/2:
                        power_apple.rect.x -= 3
                    if apple.rect.y > Ltela/2-270:
                        power_apple.rect.y -= 3
                power_apple.cair()
                if power_apple < Htela:
                    multiplicador = 1
                    power_apple_group.remove(power_apple)
        except:''


        # intervalo minimo entre os buracos
    timer_buraco += 1
    if timer_buraco == FPS*11:
        aleatorio = randrange(1,4)
        if aleatorio <= 5:
            buraco.rect.x = 900
            lateral_buraco.rect.x = 800
        timer_buraco = 0

    # background

    sky_group.draw(tela)
    arvore_group.draw(tela)
    Score(pontuacao)
    if pontuacao < highscore:
        HighScore(highscore)
    else:
        NewHighScore(pontuacao)
    Multiplicador(multiplicador)
    heart_group.draw(tela)
    #chao
    chao_group.draw(tela)
    lateral_group.draw(tela)
    power_bar_group.draw(tela)
    #player
    player_group.draw(tela)
    #apples
    apple_group.draw(tela)
    golden_apple_group.draw(tela)
    power_apple_group.draw(tela)
    rotten_apple_group.draw(tela)
    falling_heart_group.draw(tela)

    mostrador_group.draw(tela)


    pygame.display.update()

pygame.mixer.Sound.stop(backgrond_sound)


if pontuacao > highscore:
    original = json.dumps(str(pontuacao), sort_keys = True, indent = 4)
else:
    original = str(highscore)

with open('highscore.json','w') as highscore:
    highscore.write(original)

#firebase.patch('https://highscore-global.firebaseio.com/', original)

pygame.display.quit()
