# make tuple list and number list separately
# and merge into a dictionary

def spiralNumber(row, col):
    '''
    return: prints
    '''

    # make a tuple list


    # merge the tuple list and the number list into a dictionary

    # print out the dictionary in a spiral fashion
    printNum(intoDict(intoTuple(row, col)))

def intoTuple(row, col):
    '''

    return: a tuple, of positions as keys
        len(intoTupe(row, col)) = row * col
    '''
    # into the biggest index numbers
    rowIndex = row - 1
    colIndex = col - 1

    rowFixed = True # False: columm fixed
    increasing = True # False: decreasing

    # when row index is fixed
    if rowFixed:
        # columm index in increasing order (left -> right)
        if increasing:

        # columm index in decreasing order (right -> left)
        else:

    # when columm index is fixed
    else:
        # row index in increasing order (top -> bottom)
        if increasing:
            increasing = False
        # row index in decreasing order (bottom -> top)
        else:
            increasing = True
def


def intoDict(keyList):
    '''
    keyList: a list, of positions as keys

    returns: a dict, of positions as keys and numbers as values
    '''
    numDict = {}

    for i in range(len(keyList)):
        numDict[keyList[i]] = i

    return numDict
