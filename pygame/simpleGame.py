import pygame

# from pygame.locals import *

WIDTH = 640
HEIGHT = 480
TITLE = "Simple Game"

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.clock.tick(60)
            self.draw()

    def draw(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75, 0)
        pygame.display.update()


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
