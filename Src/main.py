import random


def validate_input(guess_number):
    if guess_number.isalpha():
        print('you should input a number')
        return False
    elif not (0 < float(guess_number) < 100):
        print('The number is out of range. Please entre a number between 0 and 100')
        return False
    return True


def main():
    actual_number = random.randint(0, 100)
    score = 10
    while True:
        guess_number = input("please entre a number between 0 and 100: ")

        if guess_number == 'q':
            print("Thanke you for playing! see you latter :)")
            break
        elif score == 0:
            print('game over!!!  you lost the game :(')
            print(f'The correct answer is --> {actual_number}')
            break
        elif not validate_input(guess_number):
            continue

        guess_number = float(guess_number)

        if guess_number == actual_number:
            print('Congratulation :) you won!!!')
            play_again = input('Do you wanna play again? (yes/no): ').lower()
            if play_again == 'yes':
                actual_number = random.randint(0, 100)
                score = 10
                continue
            else:
                play_again == 'no'
                break

        if guess_number < actual_number:
            print('Try a higher number')
            score -= 1
            print(f'{score} chance left')
        elif guess_number > actual_number:
            print('Try a lower number')
            score -= 1
            print(f'{score} chance left')


if __name__ == '__main__':
    main()