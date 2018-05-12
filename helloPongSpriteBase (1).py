import pygame
import sys
from pygame.locals import *
from random import randrange

# ===============      CLASSES      ===============
class Bola(pygame.sprite.Sprite):

  def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x, vel_y):
    pygame.sprite.Sprite.__init__(self)
    self.vx = vel_x
    self.vy = vel_y
    self.image = pygame.image.load(arquivo_imagem)
    self.rect = self.image.get_rect()
    self.rect.x = pos_x
    self.rect.y = pos_y
    
  def move(self):
    self.rect.x += self.vx
    self.rect.y += self.vy
# ===============   INICIALIZAÇÃO   ===============
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Hello World')

# carrega imagem de fundo (https://wallpapersafari.com/dark-green-background/)
fundo = pygame.image.load("fundo-800X600.jpg").convert()

# cria bola (http://pngimg.com/download/10405)
bola = Bola("zombie.png", randrange(800),randrange(600), 
            randrange(-10,10), randrange(-10,10))
bola_group = pygame.sprite.Group()
bola_group.add(bola)

# ===============   LOOPING PRINCIPAL   ===============
rodando = True
while rodando:
  
  for event in pygame.event.get():  #pega lista de eventos
    if event.type == QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
      rodando = False            #executa a função de sistema "exit"
  #move a bola pela tela
  bola.move()
  if bola.rect.x < 0 or bola.rect.x > 800:
    bola.vx = - bola.vx
  if bola.rect.y < 0 or bola.rect.y > 600:
    bola.vy = - bola.vy
        
  #gera saídas
  tela.blit(fundo, (0, 0))
  bola_group.draw(tela)
  pygame.display.update()      #coloca a tela na janela
    
pygame.display.quit()