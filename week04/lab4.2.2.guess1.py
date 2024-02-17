# lab4.2.2.guess1.py
# guess the number
# Author : Rahul Parvesh Dewan

numbertoguess = 25

guess = int(input("Guess the number: "))

while guess != numbertoguess:
    print ("Wrong")
    guess = int(input("Guess the number again: "))

print("Well done! The number was {} ".format(numbertoguess))

      

