# practise an exception
# author : rahul parvesh dewan

balance = 100

def withdraw(amount):
    global balance
    if amount < 0:
        raise ValueError("Amount should be positive")
    balance -= amount
    return balance

amount = int(input("Enter amount to withdraw: "))
print(withdraw(amount))


