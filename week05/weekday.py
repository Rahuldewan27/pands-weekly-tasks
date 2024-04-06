# weekday.py
# check if today is weekday or weekendvand return output accordingly
# author: Rahul Parvesh Dewan

import datetime
#import module from datetime library

day_of_week = datetime.datetime.now().weekday()
# get the current day of the week using the datetime module but in numners

if day_of_week < 5:
    print("Yes, unfortunately today is a weekday.")
#on code check friday showed as 4, so anything less than 5 is a weekday. Print the output
else:
    print("It is the weekend, yay!")
#Anything else print this output
    
#References: 
#1. pynative. (n.d.). Python - Get the Day of Week.[https://pynative.com/python-get-the-day-of-week/](https://pynative.com/python-get-the-day-of-week/)
#2. w3schools. (n.d.). Python DateTime.[https://www.w3schools.com/python/python_datetime.asp](https://www.w3schools.com/python/python_datetime.asp)

