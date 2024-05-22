import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.generate_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def generate_random_word(self):
        return random.choice(self.word_list)

# Test the Hangman class initialization
word_list = ['apple', 'banana', 'grapes', 'kiwi', 'pineapple']
hangman_game = Hangman(word_list)
print("Word to be guessed:", hangman_game.word)
print("Word guessed so far:", hangman_game.word_guessed)
print("Number of unique letters:", hangman_game.num_letters)
print("Number of lives:", hangman_game.num_lives)
print("List of guesses:", hangman_game.list_of_guesses)
