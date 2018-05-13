import pygame

class Arvores(pygame.sprite.Sprite):
    def __init__(self, imagem, x, y, vel_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = vel_x
    def lateral(self):
        if self.rect.x >= -809:
            self.rect.x -= self.vel_x
        else:
            self.rect.x = 809