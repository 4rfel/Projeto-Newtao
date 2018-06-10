import pygame

class BuracoNegro(pygame.sprite.Sprite):
    def __init__(self, imagem,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagem).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
