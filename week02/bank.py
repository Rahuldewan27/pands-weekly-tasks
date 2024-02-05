# bank.py
# Input in cents and return euros
# Author : Rahul Parvesh Dewan

#input the number in integer
amount1 = int(input("Enter amount1(in cent) : "))
amount2 = int(input("Enter amount2(in cent) : "))

#compute the number in output format
sum = (amount1+amount2)/100

#output the number
print(f'The sum of these is €{sum}')