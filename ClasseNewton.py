import pygame
import os

ALPHA = (0,255,0)
sem_controle = False
try:
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    
except:
    sem_controle = True


class Newton(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frames = 4
        self.reverse_images = []
        for i in range(6,11):
            img = pygame.image.load(os.path.join('Newtons\\newton' + str(i) + '.png')).convert_alpha()
            img = pygame.transform.scale(img, (75, 100))
            img.set_colorkey(ALPHA)
            self.reverse_images.append(img)
            self.image = self.reverse_images[0]
            self.rect  = self.image.get_rect()
        for i in range(1,5):
            img = pygame.image.load(os.path.join('Newtons\\newton' + str(i) + '.png')).convert_alpha()
            img = pygame.transform.scale(img, (75, 100))
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()
        self.frame = 0
        self.rect.x = x
        self.rect.y = y
        self.xspeed = 0
        self.jumping = False
        self.morrendo = False        
        
    def move(self):
        self.xspeed = 0
        key = pygame.key.get_pressed()
        if sem_controle:
            if self.rect.x < 730:
                if key[pygame.K_RIGHT] or key[pygame.K_d]:
                    self.xspeed = 12
                    self.frame += 1
                    if self.frame > 3*self.frames:
                        self.frame = 0
                    self.image = self.images[self.frame//self.frames]
            if self.rect.x >=0:
                if key[pygame.K_LEFT] or key[pygame.K_a]:
                    self.xspeed = -12
                    self.frame += 1
                    if self.frame > 3*self.frames:
                        self.frame = 0
                    self.image = self.reverse_images[self.frame//self.frames]
            if not self.morrendo:
                self.rect.x += self.xspeed
            
        if not sem_controle:
            horizontalaxis = joystick.get_axis(0)
            if self.rect.x < 730:
                if horizontalaxis > 0.1:
                    self.xspeed = 12
                    self.frame += 1
                    if self.frame > 3*self.frames:
                        self.frame = 0
                    self.image = self.images[self.frame//self.frames]
            if self.rect.x >=0:
                if horizontalaxis < -0.1:
                    self.xspeed = -12
                    self.frame += 1
                    if self.frame > 3*self.frames:
                        self.frame = 0
                    self.image = self.reverse_images[self.frame//self.frames]
                    
                    
            if not self.morrendo:
                self.rect.x += self.xspeed
        
    def do_jump(self):
        key = pygame.key.get_pressed()
        if sem_controle:
            if key[pygame.K_UP] and not self.jumping or key[pygame.K_w] and not self.jumping:
                self.jumping = True
                
        if not sem_controle:
            buttonX = joystick.get_button(2)
            if buttonX:
                self.jumping = True
                
    def do(self):
        self.do_jump()
        self.move()