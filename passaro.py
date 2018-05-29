import pygame

class Passaro(pygame.sprite.Sprite):

    def __init__(self, x, y, velx):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frames = 9
        self.frame = 0
        for i in range(1,9):
            img = pygame.image.load('Passaro\\bird - Copia (' + str(i) + ').png').convert_alpha()
            img = pygame.transform.scale(img, (100,25))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velx = velx

    def move(self):
        self.rect.x -= self.velx
        self.frame += 1
        if self.frame == self.frames:
            self.frame = 0
        self.image = self.images[self.frame]
