# lab4.1.1.isEven.py
# Checks inputted integer is even or odd
# author : rahul parvesh dewan

number = int(input("Please enter an intenger: "))
if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")