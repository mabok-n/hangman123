
import random

word_list = ['apple','banana','grapes','kiwi','pineapple']
word = random.choice(word_list)
for letter in word:
    print(letter)

class Hangman:
    def __init__(self,word_list,num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = generate_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess = guess.lower()
        print(f'You guessed the letter: {guess}')
        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            


        

    def ask_for_input(self):
        while True:
            guess = input("Please input guess")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You have already tried this character!")
                break
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


def generate_random_word():
    word = random.choice(word_list)
    return word




        

hangman_game = Hangman(word_list)
hangman_game.ask_for_input()

  



    






