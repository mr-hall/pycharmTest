"""Test of pygame"""

import pygame, sys
from menus import MainMenu
from play import Play

__version__= "0.1"
__author__="G Hall"

# Testing on new pycharm
# Game Constants
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
CAPTION = "Mr Hall's Game"

class GameState():
    def __init__(self):
        self.currentState = None
        self.done = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(CAPTION)



class Game():
    def __init__(self):
        self.gameState = GameState()
        self.gameState.currentState = MainMenu()


    def main(self):
        clock = pygame.time.Clock()
        while not self.gameState.done:
            if pygame.event.get(pygame.QUIT):
                self.gameState.done = True
            self.gameState.currentState.handle_events()
            self.gameState.currentState.update()
            self.gameState.currentState.render()
            pygame.display.flip()
            clock.tick(FPS)

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.main()
    pygame.quit()
    sys.exit()
