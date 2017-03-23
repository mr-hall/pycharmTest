import pygame
import colours

class BaseMenu():
    def __init__(self, menu_items):
        self.menu_items = menu_items
        self.initFonts()

    def initFonts(self):
        size = int(100 / len(self.menu_items))
        self.font = pygame.font.SysFont("monospace", size)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(colours.BLACK)
        for i in range(len(self.menu_items)):
            text=self.font.render(self.menu_items[i],1,colours.WHITE)
            screen.blit(text,(100,100*i))

class MainMenu(BaseMenu):
    def __init__(self, game):
        self.game = game
        menu_items = ["test","test2"]
        super().__init__(menu_items)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.currentState = self.game.states["play"]
        return False