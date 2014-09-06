#!/usr/bin/python

''' This is a small assignment to solve
    Problem 6 on ProjectEuler.net
    Sum square difference
    -----------------------------------
    Sum of the squares of the first ten natural numbers is,
        1^2 + 2^2 + ... + 10^2 = 385
    Square of the sum of the first ten natural numbers is,
        (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of squares and square of the sum
    is 3025 - 385 = 2640
    Find the difference between the sum of the squares and square of the sum of
    the first 100 natural numbers
'''

def sum_squares():
    result = 0
    # range() - up to but not including end range
    for i in range(1, 101):
        result += i**2
    return result

def square_of_sum():
    total = 0
    for i in range(1,101):
        total += i

    return total**2

def main():
    sums = sum_squares()
    squares = square_of_sum()
    print "Sum of the squares: %r\n" % sums
    print "Square of Sum: %r\n" % squares
    print "Difference: %r\n" % (squares-sums)
    

if __name__== "__main__":
    main()
