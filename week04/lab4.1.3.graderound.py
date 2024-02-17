# lab4.1.3.graderound.py
# print grade based on inputted percentage
# author : Rahul Parvesh Dewan

percentage = float(input("Enter the percentage: "))
#input percentage

percentage1 = round(percentage)

if percentage1 < 0 or percentage1 > 100:
    print("Please enter a number between 0 and 100")
elif percentage1 < 40: #less than 40
    print("Fail") 
elif percentage1 < 50: #40-49
    print("Pass")
elif percentage1 < 60: #50-59
    print("Merit 1")
elif percentage1 < 70: #60-69
    print("Merit 2")
else:   #70-100
    print("Distinction")