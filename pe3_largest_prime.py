#PROJECT EULER PROBLEM #3
#The prime factors of 13195 are 5, 7, 13 and 29. 
#What is the largest prime factor of the number 600851475143?

#Generate list of prime numbers of given input

import math

#FIND FACTORS
def find_factors(x):
    factors = []
    for i in range(1, int(x*0.5)):
        if x % i != 0:
            continue
        else:
            factors.append(i)
    prime_factors=[]
    for i in factors:
        for  x in range(3, int(i**0.5)):
            if i % x == 0:
                break
            else:
                continue
            prime_factors.append(i)
    print(prime_factors)
            

isprime()
    
    
