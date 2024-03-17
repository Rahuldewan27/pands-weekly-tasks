# messing with numpy 
# author : rahul parvesh dewan

import numpy as np

list_of_numbers = [1, 2, 3, 'asdf']
list_of_numbers = list_of_numbers + [3]

print("list",list_of_numbers)

numbers = np.array((1,2,3,4))
numbers = numbers * np.array((1,2,3,4))

print("array", numbers)

rando = np.random.randint(100,200,30)
print(rando)

normalrando = np.random.normal(loc=50, scale=20, size = 100)
print(normalrando)