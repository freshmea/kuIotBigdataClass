# API 문서

이 문서는 `new-uv` 프로젝트의 클래스와 함수의 기능을 설명합니다.

## BodySegment 클래스

A class to represent a segment of the snake's body.

### Attributes

- `pos` (tuple): The position of the body segment.
- `color` (tuple): The color of the body segment.

### Methods

- `__init__(pos, color)`: Constructs all the necessary attributes for the body segment object.

## Snake 클래스

A class to represent the snake.

### Attributes

- `color` (tuple): The color of the snake.

### Methods

- `__init__(color)`: Constructs all the necessary attributes for the snake object.
- `change_direction(direction)`: Changes the direction of the snake.
  - Parameters:
    - `direction` (str): The new direction of the snake.
- `move(speed)`: Moves the snake in the current direction.
  - Parameters:
    - `speed` (int): The speed at which the snake moves.
- `update()`: Updates the snake's position.
- `grow()`: Grows the snake by adding a new segment.
- `draw(screen)`: Draws the snake on the screen.
  - Parameters:
    - `screen` (pygame.Surface): The screen to draw the snake on.

## EnemySnake 클래스

A class to represent an enemy snake.

### Methods

- `__init__()`: Constructs all the necessary attributes for the enemy snake object.
- `update()`: Updates the enemy snake's position.

## Pizza 클래스

A class to represent a pizza.

### Methods

- `__init__()`: Constructs all the necessary attributes for the pizza object.

## Game 클래스

A class to represent the game.

### Methods

- `__init__()`: Constructs all the necessary attributes for the game object.
- `run()`: Runs the game loop.
- `handle_events()`: Handles the game events.
- `update()`: Updates the game state.
- `draw()`: Draws the game elements on the screen.
