import pygame


class Newton_test(pygame.sprite.Sprite):
    def __init__(self, imagem,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def right(self):
        self.rect.x += 12
    
    def left(self):
        self.rect.x -= 12
    
    def up(self):
        self.jumping = True