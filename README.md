# Number Guessing Game

⚠️ **Warning**: This is just a simple game created in order to practice coding. **Don't waste your time** —it's just for learning purposes!

Welcome to the **Number Guessing Game**! This is a fun, interactive game where you try to guess a randomly generated number within a specific range. The game provides feedback on whether your guess is too high or too low, and the number of attempts varies based on the difficulty level chosen.

### Credits
This project is based on the Number Guessing Project from roadmap.sh.
https://roadmap.sh/projects/number-guessing-game

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How to Play](#how-to-play)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The **Number Guessing Game** is a simple Python-based game where the player must guess a randomly generated number. The player can choose from different difficulty levels, and the game gives feedback after each guess (too high, too low, or correct).

### Difficulty Levels:

- **Easy:** 10 chances to guess the number.
- **Medium:** 5 chances to guess the number.
- **Hard:** 3 chances to guess the number.
- **Default:** If an invalid difficulty level is chosen, the game defaults to "Easy" with 10 chances.

## Features

- Choose difficulty: Easy, Medium, Hard, or Default
- Random number generation within a set range (1 to 100)
- Feedback after each guess (too high, too low, or correct)
- Option to exit the game by pressing `CTRL + C`
- Handle edge cases like invalid input, out-of-range guesses, and non-numeric input

## How to Play

1. Launch the game by running the Python script.
2. Choose your desired difficulty level (Easy, Medium, or Hard).
3. Start guessing the randomly generated number. The game will give you feedback on whether your guess is too high or too low.
4. Keep guessing until you either run out of attempts or guess the correct number.
5. If you run out of attempts, the game will reveal the correct number.
6. You can exit the game anytime by pressing `CTRL + C`.

## Installation

Follow the steps below to set up and play the game:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/number-guessing-game.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd number-guessing-game
    ```

3. **Ensure you have Python installed:**

    - If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).
    
4. **Run the game script:**

    ```bash
    python3 number_guessing_game.py
    ```

## Usage

Once the game is launched, follow these instructions:

- When prompted, choose a difficulty level (1 for Easy, 2 for Medium, or 3 for Hard).
- Start guessing the number by entering your guesses and pressing `Enter`.
- After each guess, the game will give you feedback:
  - "Too high! Try again." (if your guess is greater than the correct number)
  - "Too low! Try again." (if your guess is smaller than the correct number)
  - "Congratulations! You guessed the number!" (if you guess the correct number)
- If you guess the number within the allowed attempts, you win! If not, the correct number will be revealed at the end.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

Please ensure that any changes follow the project's coding conventions and include tests for new features or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Example Usage:

```bash
───────────────────────────────────
 🎮  Choose Your Difficulty Level  🎮
───────────────────────────────────
  1️⃣  Easy    (10 attempts)
  2️⃣  Medium  (5 attempts)
  3️⃣  Hard    (3 attempts)

 🔹 Press any other number for Default (Easy)
 🔹 To exit, press CTRL + C 

 ⚠️  Warning: This game is just for coding practice, so don't waste your time if you're looking for a real game! 
───────────────────────────────────
Enter your choice: 2
You have 5 attempts to guess the number.
You have 5 attempts left. Make a guess: 50
Too high! Try again.
You have 4 attempts left. Make a guess: 30
Too low! Try again.
You have 3 attempts left. Make a guess: 40
Congratulations! You guessed the number.
```
