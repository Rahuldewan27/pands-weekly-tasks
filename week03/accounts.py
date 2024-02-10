# accounts.py
# input bank account number and replace first 6 digits with XXXXXX
# author = rahul parvesh dewan

# Initial Program
# bank_account = input("Please enter your 10 digit bank account : ")
# print("XXXXXX{}".format(bank_account[6:10]))

# modified program
# input the bank account number
bank_account = input("Please enter your bank account number : ")

#split from last 4 digits
cut_bank_account = bank_account[-4:]
#calculate length of bank account to calculate number of X to be printed
length_bankaccount = len(bank_account)
cut_length_bankaccount = length_bankaccount-4
#diplay X times of above calcluation and L4 digits of bank accounts
print("X"*cut_length_bankaccount+cut_bank_account)

# assumption: if the length of the bank account is 4 or less it will only return the exact value back