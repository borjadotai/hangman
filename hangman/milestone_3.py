import random

word_list = ["banana", "apple", "cherries", "pear", "peach"]
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if(guess in word):
        print("Good guess! {} is in the word.".format(guess))
    else:
        print("Sorry, {} is not in the word. Try again.".format(guess))

def ask_for_input():
    print('Take a guess, write one character:')
    guess = input()

    try:
        if len(guess) > 1:
            raise ValueError("The string is longer than one character.")
        elif not guess.isalpha():
            raise ValueError("The string is not alphabetical.")
        else:
            check_guess(guess)
    except ValueError as e:
        print("Invalid letter. Please, enter a single alphabetical character.")

while True:
    ask_for_input()