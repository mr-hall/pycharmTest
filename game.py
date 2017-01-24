from player import *
#Testing update
#Test update 2
class Game():
    def __init__(self):
        self.backgroundColor = WHITE
        self.sprites = pygame.sprite.Group()
        self.player = Player()
        self.sprites.add(self.player)
        self.controls = {
            pygame.K_UP: self.player.up,
            pygame.K_DOWN: self.player.down
        }

    def handleEvents(self):
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
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = Game()
    done = False
    clock = pygame.time.Clock()
    while not done:
        done = game.handleEvents()
        game.update()
        game.draw(screen)
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()
