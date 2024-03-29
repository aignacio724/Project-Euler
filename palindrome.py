#!/usr/bin/python
''' Brute force version
    Largest: 906609 993 913

    total iterations: 629


    real    0m0.203s
    user    0m0.194s
    sys     0m0.008s
'''

def main():
    result = 0
    a = 0
    b = 0
    iterations = 1
    for i in range (999, 100, -1):
        for j in range (999, 100, -1):
            product = i * j
            if str(product) == str(product)[::-1]:
                if product > result:
                    result = product
                    a = i
                    b = j
                #print "%d * %d = %d\n" % (i, j, product)                
                iterations += 1
                break

    print "Largest: %d %d %d\n" % (result, a, b)
    print "total iterations: %d\n" % iterations
    
if __name__== "__main__":
    main()
