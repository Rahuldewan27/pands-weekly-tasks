
import logging
logging.basicConfig(level=logging.DEBUG)


def fibonacci(number):
    a=0
    b=1
    fibonaccisequence = [0]
    #we have one in the list already so number - 1 times
    #this is not the most efficient code
    #could have used yield
    for i in range(1,number):
        fibonaccisequence.append(b)
        a,b = b,a+b
    
    logging.debug("%d: %s",number, fibonaccisequence)

    if number == 0:
        return fibonaccisequence

    if number < 0:
        raise ValueError('number must be > 0')

    return []

if __name__ == '__main__':
    # tests will go here
    print("all good")



try :
    fibonacci(-1)
except ValueError:
    # we want this exception to be thrown
    # so this is an example where we want to do nothing
    pass
else:
    # if the exception was not thrown we should throw
    # Assertion error
    assert False, 'fibonacci missing ValueError'
    # or
    # raise AssertionError("fibonacci no valueError ")
