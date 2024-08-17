import random


class RockPaperScissors:
    """Main class for the game rock, paper, scissors
    """
    def __init__(self) -> str:
        """Initialize the game by getting the player's name.
        """
        self.name = input("Please inter your name to start the game: ")
        print(f"Hello {self.name}\n")

    def get_choices(self) -> str:
        """Method to Obtain User and Computer Choices.

        :param choices: The possible choices
        :param user_choice: The user's choice
        :param computer_choice: The computer choice
        :return user and computer choices as a string
        """
        self.choices = ['rock', 'paper', 'scissors']
        self.user_choice = input(f'Please entre your choice from {self.choices}: ').lower()
        self.computer_choice = random.choice(self.choices)
        if self.user_choice in self.choices:
            return self.user_choice and self.computer_choice
        print(f"Invalid choice. Please entre your choice from {self.choices}: ")
        return self.get_choices()

    def winner(self) -> str:
        """Method to decide winner based on the game's rules.
        """
        winnig_combination = [['rock', 'scissors'], ['paper', 'rock'], ['scissors', 'paper']]
        if self.user_choice == self.computer_choice:
            return "It's a tie! \nYour choice is: {self.user_choice}. \nThe computer choice is: {self.computer_choice}"
        elif [self.user_choice, self.computer_choice] in winnig_combination:
            return f"Congratulations!!! You Won!!! \nYour choice is: {self.user_choice}. \nThe computer choice is: {self.computer_choice}"
        else:
            return f"Game Over!!! \nYour choice is: {self.user_choice}. \nThe computer choice is: {self.computer_choice}"

    def play(self):
        """Main method to play the game.
        """
        self.get_choices()
        print(self.winner())


if __name__ == '__main__':
    game = RockPaperScissors()

    while True:
        game.play()
        play_again = input("\nDo you want to play again? (Press any key to play again, Enter q/Q to exit.): ")
        if play_again.lower() == 'q':
            break
