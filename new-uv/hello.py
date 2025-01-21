import sys

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Hello from new-uv!")
    font = pygame.font.Font(None, 74)
    text = font.render("Hello from new-uv!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(320, 240))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()
