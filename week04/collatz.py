# collatz.py    
# asks user to input positive integer
# outputs the Collatz sequence
# Author : Rahul Parvesh Dewana

# ask user to input positive integer
pos_int = int(input("Please enter a positive integer: "))

# create an empty list
col_lst = []

# append the positive integer to the list first
col_lst.append(pos_int)

while pos_int != 1: #check if the positive integer is not equal to 1
    if pos_int%2==0: #check if the positive integer is even
        pos_int = int(pos_int/2) #divide the positive integer by 2
        col_lst.append(pos_int) # append the new positive integer to the list
    
        
    elif pos_int%2!=0: #check if the positive integer is odd
        pos_int = int(pos_int*3+1) #multiply the positive integer by 3 and add 1
        col_lst.append(pos_int) # append the new positive integer to the list


for value in col_lst: #print the Collatz sequence
    print(value, end = " ") #print the Collatz sequence in a single line

# References : 
#1. Stack Overflow. (n.d.). Making a Collatz program - Automate the Boring Stuff.[https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff](https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff)
#2. Code Review Stack Exchange. (n.d.). Automate the Boring Stuff with Python: The Collatz Sequence.[https://codereview.stackexchange.com/questions/285429/automate-the-boring-stuff-with-python-the-collatz-sequence](https://codereview.stackexchange.com/questions/285429/automate-the-boring-stuff-with-python-the-collatz-sequence)
