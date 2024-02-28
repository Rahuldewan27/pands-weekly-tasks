# lab5.3.10randomque
# author : rahul parvesh dewan

import random

queue = []
numbers=10
rangemax=100

for n in range(0,numbers):
    queue.append(random.randint(0,rangemax))

print("queue is ",queue)

while len(queue) != 0:
    current_number = queue.pop(0)
    print("current number is {} and the queue is {}".format(current_number,queue))
