# lab4.2.4.random.py
# random number between 0 and 100
# Author : Rahul Parvesh Dewan

import random

numbertoguess = random.randint(0,100)

guess = int(input("Please guess the number: "))

while guess != numbertoguess:
    if guess < numbertoguess:
        print("Too low")
    else:
        print("Too high") #only other option since can't be equal
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was", numbertoguess)
