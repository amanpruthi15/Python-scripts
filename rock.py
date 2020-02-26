#rock.py
#2-24-2020
#Aman Pruthi

import random

options = ["Rock","Paper","Scissors"]
AI = random.choice(options)
user = input("Pick either Rock, Paper or Scissors: ")
user = user.lower()

if user == 'rock':
    if AI == 'Rock':
        print ('Tie Game')
    elif AI == 'Paper':
        print ('AI Wins')
    else:
        print ('User Wins')
if user == 'paper':
    if AI == 'Rock':
        print ('User Wins')
    elif AI == 'Paper':
        print ('Tie Game')
    else:
        print ('AI Wins')
if user == 'scissors':
    if AI == 'Rock':
        print ('AI Wins')
    elif AI == 'Paper':
        print ('User Wins')
    else:
        print ('Tie Game')
