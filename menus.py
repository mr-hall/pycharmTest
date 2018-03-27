import pygame
import colours
from tools import State
import play



class MainMenu(State):
    def __init__(self):
        super().__init__()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

    def update(self):
        pass

    def render(self):
        pass
