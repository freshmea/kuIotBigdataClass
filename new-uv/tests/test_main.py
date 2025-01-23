import pygame
import pytest

from new_uv.main import BodySegment, EnemySnake, Game, Pizza, Snake


@pytest.fixture
def game():
    pygame.init()
    return Game()

def test_snake_initial_position():
    snake = Snake((255, 255, 255))
    assert snake.snake_pos == [100, 150]

def test_snake_move():
    snake = Snake((255, 255, 255))
    snake.change_direction('UP')
    snake.move(10)
    assert snake.snake_pos == [100, 140]

def test_enemy_snake_initial_position():
    enemy_snake = EnemySnake()
    assert 0 <= enemy_snake.snake_pos[0] <= 800
    assert 100 <= enemy_snake.snake_pos[1] <= 600

def test_pizza_initial_position():
    pizza = Pizza()
    assert 0 <= pizza.rect.topleft[0] <= 800 - pizza.size
    assert 100 <= pizza.rect.topleft[1] <= 600 - pizza.size

def test_game_initialization(game):
    assert game.screen.get_size() == (800, 700)
    assert game.running is True

def test_game_run(game):
    game.running = False
    with pytest.raises(SystemExit):
        game.run()
