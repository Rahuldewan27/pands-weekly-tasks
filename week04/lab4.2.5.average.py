# lab4.2.5.average.py
# Read numbers tlil the user enters 0. Prints the numbers and their average.
# Author: Rahul Parvesh Dewan

numbers = []

number = int(input("Enter a number(0 to quit): "))

while number != 0:
    numbers.append(number)
    number = int(input("Enter another number (0 to quit): "))

for value in numbers: #Prints the numbers, once the user enters 0
    print(value)

average = float(sum(numbers)) / len(numbers) #Calculates the average of the numbers
print("The average is {}".format(average))

