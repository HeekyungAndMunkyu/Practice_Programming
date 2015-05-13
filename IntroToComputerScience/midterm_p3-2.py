def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    print 'SquareHelper(%d, %d) + %d' % (n-1, x, x)
    return SquareHelper(n-1, x) + x

x = int(raw_input('enter an integer:  '))
print Square(x)
