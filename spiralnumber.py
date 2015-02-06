# sprialnumber

def sprialNumber(col, row):
    '''
    col: int >= 1, columm
    row: int >= 1, row

    return: prints numbers from 0 to (col * row - 1) in a sprial fashion

        ex)
        col = 6, row = 6

        (picture)

    '''
    # make a dictionary of numbers as values (int) and position as keys (tuple)
    # ex) {(0,0): '0', (0,1): '1'}

    # print the dictionary in a sprial fashion
    printSpiral(intoDict(col, row))

def intoDict(col, row):
    '''
    col: int >= 1, columm
    row: int >= 1, row

    return: dict, keys = positions in tuple, values = numbers in int
        ex)
        col = 3, row = 1
        {(0,0): '0', (0,1): '1', (0,2): '2'}
    '''
    # number variable
    num = None


    # make position keys with tuples

    # when y's position is fixed and only x's position is changing
        # for y's position
        for yPosition in range(0, row):
            # for x's position
            for xPosition in yFixedAssignTuple(yPosition, xPosition)

    # when x's position is fixed and only y's position is changing

def printSprial(numDict):
    '''
    numDict: dict, of numbers with position as keys

    return: prints numbers in a specified position
    '''




raw_input('columm:  ')
raw_input('row:  ')
printSpiral(into(col, row))
