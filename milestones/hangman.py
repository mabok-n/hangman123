'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random
def generate_random_word():
    """
    Generate a random from the word list that is passed in a parametre

    Returns:
    - str: A random word from the word list
    
    """
    word = random.choice(word_list)
    return word
    
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
        self.word = generate_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len((self.word))
        self.num_lives = num_lives
        self.list_letters = []
        
        # Messages to be printed when game intialises
        print(f'The mistery word has {self.num_letters} characters')
        print(f'{self.word_guessed}')
        
        
    def check_letter(self, letter):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        letter = letter.lower()
        letter_found = False
        
        if letter in self.word:
            
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
            for index, letter_in_word in enumerate(self.word):
                if letter == letter_in_word  and self.word_guessed[index] == '_':
                    self.word_guessed[index] = letter
                    letter_found = True
            
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
                if letter_found == True:
                    self.num_letters -= 1
                
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        else:
            self.num_lives -= 1
        # TO DO 4 Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, 
        # print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. 
        # If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method
        while True:
            letter = input("Please guess a letter")
            if len(letter) != 1 or not letter.isalpha():
                print("Please, enter just one character")
            elif letter in self.list_letters:
                print(f'{letter} was already tried')
            else:
                self.check_letter(letter)
                self.list_letters.append(letter)

        pass

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations! You won!"
    # If the user runs out of lives, print "You lost! The word was {word}"
    while True:
        game.ask_letter()
        #continuosly checks if game.num_lives == 0 if true message is printed and breaks out of loop
        if game.num_lives == 0:
            print('You lost!')
            break
        else:
            # if game.num_lives =! 0 and game.num_letters !> 0 user has won the game
            print('Congratulations. You won the game!')
            break



if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)

# %%
