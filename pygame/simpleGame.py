import random

import pygame

# from pygame.locals import *

WIDTH = 640
HEIGHT = 480
TITLE = "Simple Game"
class BlueCircle(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group) #type: ignore
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.radius = random.randint(10, 20)
        self.speed = random.randint(1, 3)
        self.color = (0, 0, 255)
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.image.set_colorkey((255, 255, 255))

    def update(self):
        self.rect.center = (self.x, self.y)
        self.x += self.speed
        if self.x > WIDTH:
            self.x = 0
        if self.y > HEIGHT:
            self.y = 0
        if self.x < 0:
            self.x = WIDTH
        if self.y < 0:
            self.y = HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        for _ in range(30):
            self.all_sprites.add(BlueCircle(self.all_sprites))

    def run(self):
        while True:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        pygame.display.update()


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
