# sqaureroot.py
# This program calculates the square root of a number using the Newton-Raphson method
# Author: Rahul Parvesh Dewan

#define the function
def sqrt(n):
#inital guess for the square root for both side of the equation
    approx = n/2
    closer = (approx + n/approx)/2
#if both sides of the equation are not equal then start loop to guess further
    while closer !=approx:
        approx = closer
        closer = (approx + n/approx)/2
#return the result to the round function to round the result to 1 decimal place
    return round((approx),1)

#ask the user to input a positive number
n = float(input("Please enter a positive number: "))
#print the result
print(f"The square root of {n} is approx. {sqrt(n)}.")

#References :
#https://www.geeksforgeeks.org/round-function-python/
#https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
#https://www.w3schools.com/python/python_functions.asp
#https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm
