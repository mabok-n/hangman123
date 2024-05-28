import random


class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        # Initialise the attributes as indicated in the docstring
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len((self.word))
        self.num_lives = num_lives
        self.list_letters = []
        
        # Messages to be printed when game intialises
        print(f'The mistery word has {self.num_letters} characters')
        print(f'{self.word_guessed}')

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
       
        letter = letter.lower()
        if letter in self.word:
            letter_count = 0
            for index,letter_in_word in enumerate(self.word):
                if letter_in_word == letter:
                    letter_count += 1
                    self.word_guessed[index] = letter
            self.num_letters -= letter_count
            print(f"Good guess! {letter} is in the word.")
            print(self.word_guessed)
            print(f'number of letters remaing:{self.num_letters}')
        else:
            self.num_lives -= 1
            print(f'Sorry, {letter} is not in the word')
            print(f'You have {self.num_lives} ;lives left')

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
     
        while True:
            letter = input("Please input guess")
            if len(letter) != 1 or not letter.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character")
            elif letter in self.list_letters:
                print("You have already tried this character!")
            else:
                self.check_letter(letter)
                self.list_letters.append(letter)
                break

def play_game(word_list):
    """
    initialises the Hangman game by creating game an instance of the class Hangman
    passing in word_list and num_lives = 5 as parametres

    asks user for input by calling the method game.ask_letter()

    checks if num_lives and num_letters are not == 0
    whilst these condition are not met it continously ask user for a letter

    Parameters:
        ----------
        word_list: list
            List of words to be used in the game

    """

    # creates a new instance of the class Hangman as game passing in word_list, num_lives as parametres
    game = Hangman(word_list,num_lives=5)
    # while loop 
    while True:
        game.ask_letter()
        
        #continuosly checks if game.num_lives == 0 if true message is printed and breaks out of loop
        if game.num_lives == 0:
            print('You lost!')
            break
       
        if game.num_letters == 0:
            # if game.num_letters = 0 then the game is won
            print('Congratulations. You won the game!')
            break


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)