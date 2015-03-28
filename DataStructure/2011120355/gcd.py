# Euclidean Greast Common Divisor
def gcd(a, b):
    '''
    a, b: int

    returns: int, greatest common divisor
    '''
    if a == 0:
        return b

    elif b == 0:
        return a

    else:
        print b, a % b
        return gcd(b, a % b)

a, b = raw_input('Enter two integers, separated by \',\' :  ').split(',')
a = int(a)
b = int(b)

print gcd(a, b)
