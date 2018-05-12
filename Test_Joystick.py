import pygame, sys, time

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption('Controle')

interval = 0.01

loopQuit = False
while loopQuit == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loopQuit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loopQuit = True
    
   #analogicos, eles tambem pegam os comandos das setinhas
    # analogico da esquerda
   
    verticalaxis = joystick.get_axis(1)
    if verticalaxis < -0.1:
         print('pulo')
    if verticalaxis > 0.1:
        print('baixo')
    horizontalaxis = joystick.get_axis(0)
    if horizontalaxis < -0.1:
        print('esquerda')
    if horizontalaxis > 0.1:
         print('direita')
    
        
    # botoes normais - eles retornam True e False
    TRIANGULO = joystick.get_button(0)
    CIRCULO = joystick.get_button(1)
    X = joystick.get_button(2)
    QUADRADO = joystick.get_button(3)
    L1 = joystick.get_button(4)
    L2 = joystick.get_button(4)
    R1 = joystick.get_button(6)
    R2 = joystick.get_button(7)
    SELECT = joystick.get_button(8)
    START = joystick.get_button(9)
    L3 = joystick.get_button(10)
    R3 = joystick.get_button(11)


    # exemplo de codigo:
    if X:
        print('apertou o x')

    pygame.display.update()
    time.sleep(interval)

pygame.quit()
sys.exit()
