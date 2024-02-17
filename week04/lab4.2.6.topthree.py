# lab 4.2.6.topthree.py
# prints the top three numbers out of 10 randomly generated numbers between 0 and 100.

import random

how_many = 10
top = 3
start_range = 0
end_range = 100

numbers = []

for i in range(0, how_many):
    numbers.append(random.randint(start_range, end_range))
print("{} random numbers\t{}".format(how_many, numbers))

top_numbers = numbers.copy()

top_numbers.sort(reverse = True)
print("The top {} numbers are \t{}".format(top, top_numbers[0:top]))




