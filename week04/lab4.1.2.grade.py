# lab4.1.2.grade.py
# print grade based on inputted percentage
# author : Rahul Parvesh Dewan

percentage = float(input("Enter the percentage: "))
#input percentage

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40: #less than 40
    print("Fail") 
elif percentage < 50: #40-49
    print("Pass")
elif percentage < 60: #50-59
    print("Merit 1")
elif percentage < 70: #60-69
    print("Merit 2")
else:   #70-100
    print("Distinction")