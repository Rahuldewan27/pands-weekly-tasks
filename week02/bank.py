# bank.py
# Input in cents and return euros
# Author : Rahul Parvesh Dewan

#input the numbers in integer format
amount1 = int(input("Enter amount1(in cent) : "))
amount2 = int(input("Enter amount2(in cent) : "))

#compute the number i.e add the numbers and then divide by 100 to get the sum in euros
sum = (amount1+amount2)/100

#output the number
print(f'The sum of these is €{sum}')