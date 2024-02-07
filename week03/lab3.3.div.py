# lab3.3.div.py
# this will input 2 numbers, divide them and return the value and remainder
# author : rahul parvesh dewan

# input 2 variables
x = int(input("Enter First Number : "))
y = int(input("Enter the number you want to divide by : "))

# divide the number
answer = int(x//y)
remainder = x%y

# print the above
print ("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))
