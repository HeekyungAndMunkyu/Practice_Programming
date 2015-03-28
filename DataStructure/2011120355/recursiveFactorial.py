# recursive factorial

def recursiveFactorial(n):
    '''
    n: int

    returns: int, product of all the integers from 1 to it self (n > 0)
            if n == 0, returns 1

            ex. recursiveFactorial(0) == 1
                recursiveFactorial(3) == 3 * 2 * 1
    '''

    # base case: fact(0) = 1
    if n == 0:
        return 1
    # recursive case: fact(n) = n * fact(n-1)
    else:
        return n * recursiveFactorial(n-1)




n = int(raw_input('Enter an integer: '))
print 'Factorial of %d is %d' % (n, recursiveFactorial(n))
