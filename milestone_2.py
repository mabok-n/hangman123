# Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.
import random

# Step 1 Create a list containing the names of your 5 favorite fruits.
# Step 2 Assign this list to a variable called word_list.
word_list = ['apple','banana','grapes','kiwi','pineapple']

#Step 2 Print out the newly created list to the standard output (screen).
print(word_list)

# Print out word to the standard output. Run the code several times and observe the words printed out after each run.
for i in range(1,10):
    # Assign the randomly generated word to a variable called word.
    word = random.choice(word_list)
    print(word)


# Using the input function, ask the user to enter a single letter.
# Assign the input to a variable called guess.
    
guess = input('Please input your guess')

# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
#In the body of the if statement, print a message that says "Good guess!".
if guess.isalpha() and len(guess) == 1:
    print(f"Good Guess! You guessed {guess}")

# Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.
else:
    print("Ooops! That is not a valid input. Try again!")
    guess = input('Please input your guess')














