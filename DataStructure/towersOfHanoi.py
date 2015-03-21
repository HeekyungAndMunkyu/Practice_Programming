# towers of hanoi
def hanoi(n, source, middle, dest, result = []):
    '''
    n: int, number of disks
    source: str, starting point (A, B or C)
    middle: str, not starting point nor destination (A, B or C)
    dest: str, destination (A, B or C)
    result: list, of process

    retuns: list, updated result
        ex. move from A to C
            move from A to B
    '''

    # base case
    if n == 1:
        result.append('move from %s to %s' % (source, dest))
        return result
    # general case
    else:
        return hanoi(n-1, source, dest, middle, []) + \
        ['move from %s to %s' % (source, dest)] +\
        hanoi(n-1, middle, source, dest, [])

n = int(raw_input('Enter the number of disks: '))
print '\n'.join(hanoi(n, 'A', 'B', 'C', ))
