import pygame

class Apple(pygame.sprite.Sprite):
    def __init__(self, imagem,x, y,vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = vel_y
    def cair(self):
        self.rect.y += self.vel_y