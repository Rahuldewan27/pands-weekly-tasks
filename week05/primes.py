import math
# generateprimes
# author : Rahul Parvesh Dewan

primes = []
upto = 1001

for candidate in range(2, upto):
    #print (candidates)
    isPrime = True
    for divisor in primes:
        if candidate % divisor == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(candidate)

print(primes)