# towers of hanoi
def hanoi(n, source, middle, dest):
    '''
    n: int, number of disks
    source: str, starting point (A, B or C)
    middle: str, not starting point nor destination (A, B or C)
    dest: str, destination (A, B or C)

    retuns: print process
        ex. move from A to C
            move from A to B
    '''

    # base case
    if n == 1:
        print 'move from %s to %s' % (source, dest)
    # general case
    else:
        hanoi(n-1, source, dest, middle)
        print 'move from %s to %s' % (source, dest)
        hanoi(n-1, middle, source, dest)

n = int(raw_input('Enter the number of disks: '))
hanoi(n, 'A', 'B', 'C')
