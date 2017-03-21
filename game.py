"""Test of pygame"""

import pygame, sys
from play import *

__version__= "0.1"
__author__="G Hall"

# Testing on new pycharm
# Game Constants
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
CAPTION = "Mr Hall's Game"

class Game():
    def __init__(self):
       self.play = Play()

    def handle_events(self):
        return self.play.handle_events()

    def update(self):
        self.play.update()

    def draw(self, screen):
       self.play.draw(screen)

    def main(self):
        done = False
        clock = pygame.time.Clock()
        while not done:
            done = game.handle_events()
            game.update()
            game.draw(screen)
            clock.tick(FPS)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    game = Game()
    game.main()
    pygame.quit()
    sys.exit()
