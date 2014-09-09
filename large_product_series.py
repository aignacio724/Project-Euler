#!/usr/bin/python

''' Project-Euler Problem 8
    -----------------------------------------
    Find the thirteen adjacent digits in the 1000-digit number
    that have the greates product.  What is the value of this product?
'''

# This problem will be solved using sliding window
# For a Four digit number (9*9*8*9) largest product was 5832

from sys import argv

# This is our sliding window function, 
def slidingWindow(sequence,winSize):
    item = iter(sequence)
    
    window = []
    for i in range(0, winSize):
        window.append(next(item))
    yield window
    
    for value in item:
        window = window[1:] + [value]
        yield window

# Read in 1000 digit number from file
# remove the newline, if there is one
infile = open(argv[1])
lines = infile.read().strip('\n')
infile.close()
size = 13

# Build the list of the 'lists' of chunk size
window = list(slidingWindow(list(lines),size))

# Initialize some values
largest_product = -1
product = 1

# Iterate over each window and find the product of each
# Obtain the largest of all the products
for nums in window:
    #print nums
    for digit in nums:
        #print digit,
        product *= int(digit)
    #print " product::%r" % product

    if product > largest_product:
        #print "largest product::%r" % largest_product
        largest_product = product
    product = 1

print largest_product
