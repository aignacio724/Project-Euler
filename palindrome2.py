#!/usr/bin/python

''' This is a small assignment to solve
    Problem 4 on ProjectEuler.net.
    Largest Palindrome Product
    -------------------
    A palindromic number reads the same both ways. The largest palindrome made 
    from the product of two 2-digit numbers is 9009 = 91 * 99
    Find the largest palindrome made from the product of two 3-digit numbers
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
    a = ceil(sqrt(N)) # Get the Square root of N 
                      # Rounded up to the next integer
    b = a*a - N
    c = floor(sqrt(b)) # I could type cast to int, but that adds more time to 
                       # the runtime of program

    # Continue to check each value of b
    # while b is not square
    while c*c != b: 
        a = a+1
        b = a*a - N
        c = floor(sqrt(b))

    # Return the two factors of N
    return (a - sqrt(b), a + sqrt(b)) 

def main():

    curNum = 997 # Maximum number is 999 * 999 = 998001
                 # largest palidrome that is under 998001 
                 # 997799
    iterations = 1

    for i in range(997, 100, -1):
        palindrome = str(i) + str(i)[::-1]
        (val1, val2) = FermatFactor(float(palindrome))
        #### Must undesrtand why a 3 digit float returns length of 5
        if (len(str(val1)) == 5) and (len(str(val2)) == 5):
            break
        iterations += 1

    print "Largest Palindrome: %s Factors: %d %d\n" % (palindrome,val1,val2)
    print "Iterations: %d\n" % iterations

if __name__== "__main__":
    main()
'''
Largest Palindrome: 906609 Factors: 913 993

Iterations: 92


real    0m0.189s
user    0m0.188s
sys 0m0.000s
'''
