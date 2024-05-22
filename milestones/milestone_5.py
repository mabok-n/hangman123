
import random

word_list = ['apple','banana','grapes','kiwi','pineapple']
word = random.choice(word_list)

def generate_random_word():
    """
    Generate a random from the word list that is passed in a parametre

    Returns:
    - str: A random word from the word list
    
    """
    word = random.choice(word_list)
    return word

def play_game(word_list):
    """

    Play a game of Hangman with a random word generated from given wordlist

    Parameters:
    - word_list: a list of words for the game

    Returns:
    -None
   
    """
    #Number of lives set to default as 5
    num_lives = 5
    # creates a new instance of the class Hangman as game passing in word_list, num_lives as parametres
    game = Hangman(word_list,num_lives)
    # while loop 
    while True:
        #continuosly checks if game.num_lives == 0 if true message is printed and breaks out of loop
        if game.num_lives == 0:
            print('You lost!')
            break
        # continuosly checks if game.num_letters > 0 and asks user for input
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            # if game.num_lives =! 0 and game.num_letters !> 0 user has won the game
            print('Congratulations. You won the game!')
            break

class Hangman:
    """

    A class to represent a Hangman game.

    Attributes:
    
    word_list: list
        A list of possible words for the game
    num_lives: int
        The number of lives a player has, set as a default values of 5
    word: str
        calls the function generate_random_word and returns a word for the player to guess
    word_guess : list
        holds blanks spaces "_" that correspond to the number of letters in the word to be guessed
        with each correct guess the letter guessed replaces a "_" in the word
    num_letters: int
        this holds the legnth of letters in the word that the player will guess
    list_of_guesses: list
        list of values of guesses that the user inputs 
    
    
    Methods:

    check_guess(guess):
        Checks if the guessed letter is in the word and updates the game state.
    ask_for_input():
        Prompts the user for a letter guess and handles input validation.

    
    """
    def __init__(self,word_list,num_lives = 5):
        """
    Initialises the Hangman game with a list of words and a specified number of lives.
    
    Parameters
    ----------
    word_list : list
        A list of words for the game.
    num_lives : int, optional
        The number of lives the player has. Default is 5.
        """


        self.word_list = word_list
        self.num_lives = num_lives
        self.word = generate_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len((self.word))
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess = guess.lower()
        print(f'You guessed the letter: {guess}')
        
        if guess in self.word:
            letter_count = 0
            print(f"Good guess! {guess} is in the word.")
            for index,letter in enumerate(self.word):
                if letter == guess:
                    letter_count += 1
                    self.word_guessed[index] = guess
            self.num_letters -= letter_count
            print(self.word_guessed)
            # remove
            print(f'number of letters remaing:{self.num_letters}')
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} ;lives left')
        

    def ask_for_input(self):
        while True:
            guess = input("Please input guess")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You have already tried this character!")
            elif self.num_letters == 0 or self.num_lives == 0:
                print("Game Over")
                break
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)










    






