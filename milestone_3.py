import random

word_list = ['apple','banana','grapes','kiwi','pineapple']
word = random.choice(word_list)

def generate_random_word():
    word = random.choice(word_list)
    return word

#Create check guess function
#Step 1 check guess function with guess passed in as parametre
def check_guess(guess):
#Step 2 convert guess to lowercase
    guess = guess.lower()
    print(f'You guessed the letter: {guess}')
#Step 3 place code here to check if the guess is in the word
    word = generate_random_word()
    print(f'the word is {word}')
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print("Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input('Please input your guess: ')

        if guess.isalpha() and len(guess) == 1:
            print(f"Good Guess! You guessed {guess}")
            break
        else:
            print("Invalid letter. Please enter a single alphabetical character.")
    
    check_guess(guess)



    



#Test check guess function

ask_for_input()

