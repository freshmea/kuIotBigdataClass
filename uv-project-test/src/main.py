import sys

import pygame

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('지렁이 게임')

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 채우기
    screen.fill(BLACK)

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
