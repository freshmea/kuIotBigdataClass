import random
import sys
import time

import pygame

# 게임 속도 조절 변수
GAME_SPEED = 10

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.snake_pos = [100, 150]  # 초기 위치를 100, 150으로 변경
        self.snake_body = [[100, 150], [90, 150], [80, 150]]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.rect = pygame.Rect(self.snake_pos[0], self.snake_pos[1], 10, 10)

    def change_direction(self, direction):
        if direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def update(self):
        if self.direction == 'UP':
            self.snake_pos[1] -= 10
        if self.direction == 'DOWN':
            self.snake_pos[1] += 10
        if self.direction == 'LEFT':
            self.snake_pos[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_pos[0] += 10

        # 화면을 넘어가는 경우 반대쪽에서 나오게 처리
        if self.snake_pos[0] < 0:
            self.snake_pos[0] = 800
        elif self.snake_pos[0] > 800:
            self.snake_pos[0] = 0
        if self.snake_pos[1] < 100:  # 상단 100 픽셀을 고려
            self.snake_pos[1] = 600
        elif self.snake_pos[1] > 600:
            self.snake_pos[1] = 100

        self.snake_body.insert(0, list(self.snake_pos))
        self.snake_body.pop()

        # rect 업데이트
        self.rect.topleft = self.snake_pos

    def draw(self, screen, color):
        for pos in self.snake_body:
            pygame.draw.rect(screen, color, pygame.Rect(pos[0], pos[1], 10, 10))

class EnemySnake(Snake):
    def __init__(self):
        super().__init__()
        self.snake_pos = [random.randint(0, 800), random.randint(100, 600)]
        self.snake_body = [self.snake_pos] + [[self.snake_pos[0] - 10 * i, self.snake_pos[1]] for i in range(1, 5)]
        self.rect = pygame.Rect(self.snake_pos[0], self.snake_pos[1], 10, 10)
        self.move_count = 0

    def update(self):
        if self.move_count % 3 == 0:
            directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
            self.change_direction(random.choice(directions))
        self.move_count += 1

        if self.direction == 'UP':
            self.snake_pos[1] -= 10
        if self.direction == 'DOWN':
            self.snake_pos[1] += 10
        if self.direction == 'LEFT':
            self.snake_pos[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_pos[0] += 10

        # 화면을 넘어가는 경우 반대쪽에서 나오게 처리
        if self.snake_pos[0] < 0:
            self.snake_pos[0] = 800
        elif self.snake_pos[0] > 800:
            self.snake_pos[0] = 0
        if self.snake_pos[1] < 100:  # 상단 100 픽셀을 고려
            self.snake_pos[1] = 600
        elif self.snake_pos[1] > 600:
            self.snake_pos[1] = 100

        self.snake_body.insert(0, list(self.snake_pos))
        if len(self.snake_body) > 5:
            self.snake_body.pop()

        # rect 업데이트
        self.rect.topleft = self.snake_pos

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 700))  # 화면 높이를 700으로 변경
        pygame.display.set_caption('지렁이 게임')
        self.clock = pygame.time.Clock()
        self.running = True

        # 색상 정의
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)

        # 지렁이 객체 생성
        self.snake = Snake()
        self.snake_group = pygame.sprite.GroupSingle(self.snake)

        # 적 지렁이 객체 생성
        self.enemies = pygame.sprite.Group()
        for _ in range(10):
            enemy = EnemySnake()
            self.enemies.add(enemy)

        # 게임 시작 시간
        self.start_time = time.time()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(GAME_SPEED)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.snake.change_to = 'UP'
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.snake.change_to = 'DOWN'
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.snake.change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.snake.change_to = 'RIGHT'

    def update(self):
        self.snake.change_direction(self.snake.change_to)
        self.snake_group.update()
        self.enemies.update()

        # 충돌 체크
        if pygame.sprite.spritecollideany(self.snake, self.enemies):
            self.running = False

    def draw(self):
        self.screen.fill(self.BLACK)
        self.snake.draw(self.screen, self.WHITE)
        for enemy in self.enemies:
            enemy.draw(self.screen, self.RED)

        # 경과 시간 계산
        elapsed_time = time.time() - self.start_time
        font = pygame.font.SysFont(None, 36)
        time_text = font.render(f'Time: {int(elapsed_time)}s', True, self.WHITE)
        self.screen.blit(time_text, (10, 10))

        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
