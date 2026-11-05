import random


def random_number():
    """Make the computer pick a random number to display."""
    return random.randint(1, 100)

difficulty_level = {
    "easy": 10,
    "hard": 3
}

def get_user_level():
    """Returns a int that represents the attemps the user will have."""
    while True:
        try:
            user_difficulty = difficulty_level[input("Pick your difficulty: 'easy' or 'hard'\n> ")]
        except KeyError:
            continue
        else:
            return user_difficulty

def too_low_too_high(n_guess_user, n_computer):
    """Compares the number of the user to the number they trynna guess.
    Prints a hint."""
    if n_guess_user > n_computer:
        print("Too high")
    elif n_guess_user < n_computer:
        print("Too low.")



def number_guess_game():
    attempts = get_user_level()
    number_computer = random_number()
    is_on = True

    print("I'm thinking a number between 1 to 100... Can you guess which one it is?")

    while is_on:
        if attempts == 0:
            print(f"YOU LOST.\nThe number was:{number_computer}")
            is_on = False
        else:
            print(f"Your current attempts: {attempts}")
            try:
                guess_user = int(input("> "))
            except ValueError:
                print("NOT A VALID VALUE")
                attempts -= 1
            else:
                if guess_user == number_computer:
                    print(f"YOU GUESSED IT!\nThe number was {number_computer}")
                    is_on = False
                else:
                    too_low_too_high(n_guess_user=guess_user,
                                     n_computer=number_computer)
                    attempts -= 1


if __name__ == "__main__":
    number_guess_game()