#!/usr/bin/python

''' This is a small assignment to solve
    Problem 3 on ProjectEuler.net.
    Largest Prime Factor
    -------------------
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
'''

from math import ceil,floor,sqrt

''' This function will take in a given number N
    and using Fermat's Factorization Algorithm
    Try to find the largest prime factors of the given
    number N '''
# Fermat's Method:
# N = a^2 - b^2
# N should be an odd number
def FermatFactor(N):
    #print N
    #if N == 1:
    #    return N
    
    a = ceil(sqrt(N)) # Get the Square root of N 
                      # Rounded up to the next integer
    b = a*a - N
    c = floor(sqrt(b))
    # Continue to check each value of b
    # while b is not square
    while c*c != b: 
        a = a+1
        b = a*a - N
        c = floor(sqrt(b)) 
     
    #FermatFactor(a-sqrt(b))
    #FermatFactor(a+sqrt(b))
    # Return the two factors of N
    return (a - sqrt(b), a + sqrt(b)) 

def isPrime(num):
    for i in range(2,floor(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def main():
        val = float(raw_input("Enter a number to factorize "))
        #print "%d %d\n" % FermatFactor(val)
        FermatFactor(val)

if __name__== "__main__":
    main()
