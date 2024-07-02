# Snake Game

This is a classic Snake game implemented in Python using the Pygame library. The game involves controlling a snake to eat food items and grow in length while avoiding collisions with itself.

## Versions

- v0.1.0-alpha.1: initial release [2424/07/02]

## Features

- Control the snake using the arrow keys.
- Eat food items to grow in length and increase your score.
- Avoid colliding with the snake's own body.
- Save high scores and display the top 5 scores.

## Installation

1. Ensure you have Python installed on your system.
2. Install the required dependencies using pip:
    ```sh
    pip install pygame
    ```

## Running the Game

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the game using the following command:
    ```sh
    python main.py
    ```

## How to Play

- Use the arrow keys to control the direction of the snake.
- The objective is to eat the food items that appear on the screen.
- Each food item increases the snake's length and your score.
- Avoid colliding with the snake's own body.
- The game ends when the snake collides with itself.

## Scoring

- Each food item eaten increases your score by 10 points.
- The game displays your score in the top-left corner of the screen.

## Game Over

- When the game ends, the screen displays a message based on your performance and ranking.
- Press `1` to play again or `2` to exit the game.
- The top 5 scores are displayed on the game over screen.

## Code Structure

- `config.py`: Contains configuration constants for the game.
- `display.py`: Handles drawing the snake, food, and score on the screen.
- `events.py`: Handles user input and game events.
- `food.py`: Manages the generation and collision detection of food items.
- `game.py`: Contains the main game loop and game logic.
- `score.py`: Manages saving and retrieving high scores.
- `main.py`: Entry point for running the game.

## Dependencies

- `pygame`: A Python library for creating games and multimedia applications.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
