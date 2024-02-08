# lab3.6.randomfruit.py
# prints out random fruit from a list
# author rahul parvesh dewan

import random

fruits = ('Apple', 'Orange', 'Banana', 'Pear')

# assigning number to each fruit above
index = random.randint(0,len(fruits)-1)

#print friuit display
fruit = fruits[index]
print("A Random Fruit : {}" .format(fruit))
