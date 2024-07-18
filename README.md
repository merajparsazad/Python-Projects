# Number Guessing Game


Welcome to the Number Guessing Game! This is a simple command-line game where the player has to guess a randomly generated number between 0 and 100. The player has 10 chances to guess the correct number.

## How To Play

1. Run the program.
2. The program will prompt you to enter a number between 0 and 100.
3. Enter your guess.
* If your guess is correct, you win!
* If your guess is too low, the program will prompt you to try a higher number.
* If your guess is too high, the program will prompt you to try a lower number.
4. You have 10 attempts to guess the correct number.
5. If you want to quit the game at any time, type 'q'.
6. If you run out of attempts, the game will end and reveal  the correct number.
7. After winning or losing, you will be asked if you want to play again. Type 'yes' to play again or 'no' to quit.

## How To Run

1. Open your terminal or command prompt.

2. Navigate to the directory (number_guesser).

3. Set the `PYTHONPATH`:

```Bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

4. Run the game using Python:

```Bash
python main.py
```