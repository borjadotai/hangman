import random

word_list = ["banana", "apple", "cherries", "pear", "peach"]
word = random.choice(word_list)

print('Take a guess, write one character:')
guess = input()

try:
    if len(guess) > 1:
        raise ValueError("The string is longer than one character.")
    elif not guess.isalpha():
        raise ValueError("The string is not alphabetical.")
    else:
        print("Good guess!")
except ValueError as e:
    print("Oops! That is not a valid input.")