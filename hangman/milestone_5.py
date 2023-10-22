import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if(guess in self.word):
            print("Good guess! {} is in the word.".format(guess))
            for (i, char) in enumerate(self.word):
                if(guess == char):
                    self.word_guessed[i] = guess
            self.num_letters-=1
        else:
            self.num_lives-=1
            print("Sorry, letter {} is not in the word.".format(guess))
            print("You have {} lives left.".format(self.num_lives))

    def check_single_alpha(self, guess):
        if len(guess) > 1 or not guess.isalpha():
            return False
        else:
            return True

    def ask_for_input(self):
        print('Take a guess, write one character:')
        guess = input()

        try:
            if self.check_single_alpha(guess):
                if guess in self.list_of_guesses:
                    print('You already tried that letter!')
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
            else:
                raise ValueError("Invalid letter. Please, enter a single alphabetical character.")
        except ValueError as e:
            print("Invalid letter. Please, enter a single alphabetical character.")

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")

play_game(["apple", "banana"])