"""Test of pygame"""

import pygame, sys
from menus import MainMenu
from play import Play


__version__= "0.1"
__author__="G Hall"

# Game Constants
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
CAPTION = "Mr Hall's Game"

class Game():
    def __init__(self):
        self.states = {
            "main": MainMenu(self),
            'play': Play(self)
        }
        self.currentState = self.states["main"]

    def handle_events(self):
        return self.currentState.handle_events()

    def update(self):
        self.currentState.update()

    def draw(self, screen):
       self.currentState.draw(screen)

    def main(self):
        done = False
        clock = pygame.time.Clock()
        while not done:
            done = game.handle_events()
            game.update()
            game.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    game = Game()
    game.main()
    pygame.quit()
    sys.exit()
