import pygame
import os

class Power_bar(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.power = 0
        for i in range(0,6):
            img = pygame.image.load(os.path.join('Power_Bar\\power_bar-' + str(i) + '.png')).convert_alpha()
            img = pygame.transform.scale(img, (int(100*1.2), int(40*1.2)))
            img = pygame.transform.flip(img,180,0)
            self.images.append(img)
            self.image = self.images[self.power]
            self.rect  = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = self.images[self.power]
