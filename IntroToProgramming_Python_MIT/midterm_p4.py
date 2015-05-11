def myLog(x, b):
    '''
    x: int>= 1
    b: int>= 2

    returns: int, log_b(x), or, the logarithm of x relative to a base b
    '''
    power = 0

    while x - b ** power >= 0:
        power += 1

    return power - 1


x = int(raw_input('x: '))
b = int(raw_input('base: '))

print myLog(x, b)
