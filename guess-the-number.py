# Guess the number
# Aman Pruthi
# March 1, 2020

########################
# Basic Steps
########################
# 1. Design a random number 
# 2. Let the user guess the number
# 3. Tell whether the number guessed is correct, too small or too big

########################
# Detailed Steps
########################
# 1. Design a random number
#   - Import random
# 2. Let the user guess the number
#   - Define the input for number
#3. Tell whether the number guessed is
#   - define for, elif and else statments
#   - print the prediction according to the guessed number

########################
# Start with the line of code
########################

# impprt random function
import random
n = random.randint(1,99)

# Telling the user to pick a number between 1 and 99
guess = int (input("Guess any number from 1 to 99: "))

# What happens after guessing the number
while n != "guess":
    print
    if guess < n:
        print ("The number guessed is too low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print ("The number guessed is too high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print ("You guessed it right!")
        break
    print
