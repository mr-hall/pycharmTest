import colours
import pygame
from player import Player


class Play():
    def __init__(self, game):
        self.game = game
        self.backgroundColor = colours.WHITE
        self.sprites = pygame.sprite.Group()
        self.player = Player()
        self.sprites.add(self.player)
        self.controls = {
            pygame.K_UP: self.player.up,
            pygame.K_DOWN: self.player.down
        }


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN :
                try:
                    self.controls[event.key](event.type)
                except:
                    pass
        return False
    def update(self):
        self.sprites.update()

    def draw(self, screen):
        screen.fill(self.backgroundColor)
        self.sprites.draw(screen)


    def main():
       None
