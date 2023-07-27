from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess, RANDOM_NUMBER, turns):
    """
    checks answer against. returns the number of turns remaining.
    """
    if guess > RANDOM_NUMBER:
        print("Too high.\nGuess again")
        return turns - 1
    elif guess < RANDOM_NUMBER:
        print("Too low.\nGuess again")
        return turns - 1

    else:
        print("You got it! The answer is {}".format(RANDOM_NUMBER))


def set_difficulty():
    text_level = input("Choice difficulty.Type 'easy' or 'hard' : ")
    if text_level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    RANDOM_NUMBER = randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != RANDOM_NUMBER:
        print("You have {} attempts to guess the number.".format(turns))
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, RANDOM_NUMBER, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return


game()
