# messingwithFunctions2.py
# more messing with functions
# author : Rahul Parvesh Dewan

print(1,2,3,  end = "\t", sep="")
print("hi")

#unnamed args
def fun1(*args):
    print(type(args))
    print(args)
    for val in args:
        print(val)

#fun1("a", "b", "c")

#keyword arguments
def fun2(**kwargs):
    print(type(kwargs))
    print(kwargs)
    #for val in args:
    #   print(val)

fun2(name="Rahul", age=32, gender="M")

#sample code
def ave(*values):
    number_of_values = len(values)
    sum=0
    for value in values:
        sum += value

    average = sum/number_of_values
    return average, sum

av1, sum_of_numbers = ave(1,2,3,4,5,6,7,8,9,10)
print(f"Average is {av1} and sum is {sum_of_numbers}")

print(ave(1,2,3,4,5,6,7,8,9,10))
        
