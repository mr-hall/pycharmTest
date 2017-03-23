import pygame
import colours

class Player(pygame.sprite.Sprite):
    ya = 0
    maxA = 10
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Graphics/PNG/playerShip1_blue.png").convert()
        self.image.set_colorkey(colours.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.image = pygame.transform.rotate(self.image,-90)

    def update(self):
        self.rect.y += self.ya

    def up(self,keytype):
        if keytype == pygame.KEYDOWN:
            self.ya = -1
        else:
            self.ya = 0



    def down(self,keytype):
        if keytype == pygame.KEYDOWN:
            self.ya = 1
        else:
            self.ya = 0

