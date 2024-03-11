
# count_e.py
# Write a program that reads in a text file and outputs the number of e's it contains, while taking the filename from an argument on the command line
# Author : Rahul Parvesh Dewan

# Import the sys module to access the command line arguments
import sys
# Import the os.path module to check if the file exists
import os.path

# Function to count the number of 'e' in the file
def count_e(filename):
    # Check if the file exists
    if not os.path.isfile(filename):
        print("File not found.")
        return
    # Open the file and read the text
    try:
        with open(filename, 'r') as file:
            text = file.read()
            # Count the number of 'e' in the text
            count = text.count('e')
            print(f"The number of 'e' in the file is: {count}")
    # Handle the FileNotFoundError exception
    except FileNotFoundError:
        print("File not found.")

# Check if the filename is provided as a command line argument
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("Enter the filename inclduing .txt at end: ")

count_e(filename)

# References:
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.geeksforgeeks.org/python-os-path-isfile-method/
# https://www.geeksforgeeks.org/python-string-count/
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/library/sys.html#sys.argv




    
   