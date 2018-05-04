import pygame

class Newton(pygame.sprite.Sprite):
    
    def __init__(self, imagem, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xspeed = 0
        self.chao = 400
        self.jumping = False
        self.falling = True
        
        
    def move(self):
        self.xspeed = 0
        key = pygame.key.get_pressed()
        if self.rect.x <=680:
            if key[pygame.K_RIGHT]:
                self.xspeed = 8
        if self.rect.x >=0:
            if key[pygame.K_LEFT]:
                self.xspeed = -8
        self.rect.x += self.xspeed
        
            
    def do_jump(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and not self.jumping and not self.falling:
            self.jumping = True
            self.falling = False

    def fall(self):
        if self.falling:
            self.rect.y += 10
            if self.rect.y == self.chao:
                self.falling = False

    def do(self):
        key = pygame.key.get_pressed()
        self.do_jump()
        self.move()
        if not key[pygame.K_SPACE]:
            self.fall()