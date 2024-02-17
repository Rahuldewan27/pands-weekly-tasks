# lab4.2.2.guess1.py
# guess the number and provide feedback if its too high or too low
# Author : Rahul Parvesh Dewan


numbertoguess = 25
guess = int(input("Please guess the number: "))

while guess != numbertoguess:
    if guess < numbertoguess:
        print("Too low")
    else:
        print("Too high") #only other option since can't be equal
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was", numbertoguess)

