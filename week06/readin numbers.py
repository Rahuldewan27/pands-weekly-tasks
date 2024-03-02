# readin numbers.py
# multiple 2 inputted numbers
# author : Rahul Parvesh Dewan

def readNum(message = "Enter a number: "):
    num=False
    while (not num):
        try :
            num= int(input(message))
        except ValueError:
            (print("Not a number", end=" "))
    return num

num1 = readNum()
num2 = readNum("Enter another number: ")

answer = num1 * num2

print(f"The product of {num1} and {num2} is {answer}")