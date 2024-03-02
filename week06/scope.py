# scope.py
# global variables
# author : Rahul Parvesh Dewan

# I dont want to use global variables

x=999

def fun(num):
    print(num)

def fun2(x):
    print(f"in fun2 x is {x}")
    x=21
    print(f"in fun2 x is {x}")

fun2(x)
print(f"after fun2 x is {x}")
