# make tuple list and number list separately
# and merge into a dictionary

def spiralNumber(row, col):
    '''
    row: int >= 1, row
    col: int >= 1, columm

    return: prints numbers from 0 to (row * col - 1) in a sprial fashion

        ex)
        row = 6, col = 6

        0   1   2   3   4   5
        19  20  21  22  23   6
        18  31  32  33  24   7
        17  30  35  34  25   8
        16  29  28  27  26   9
        15  14  13  12  11  10

    '''

    # make a tuple list


    # merge the tuple list and the number list into a dictionary

    # print out the dictionary in a spiral fashion
    printNum(intoDict(intoTuple(row, col)), row, col)

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

    lastRow = 0
    lastCol = -1

    keyList = []

    rowDifList = range(rowIndex, -1, -1)
    colDifList = range(colIndex + 1, -1, -1)
    rowDif = 0
    colDif = 0

    print 'rowDifList:', rowDifList, '       colDifList:', colDifList

    while len(keyList) < row * col:
        # when row index is fixed
        if rowFixed:
            print 'rowFixed'
            colDif = colDifList.pop(0)
            # columm index in increasing order (left -> right)
            if increasing:
                lastRow, lastCol, keyList = tupGenRowFixed(lastRow, lastCol, colDif, keyList, increasing)
            # columm index in decreasing order (right -> left)
            else:
                lastRow, lastCol, keyList = tupGenRowFixed(lastRow, lastCol, colDif, keyList, increasing)
            rowFixed = False
        # when columm index is fixed
        else:
            print 'colFixed'
            rowDif = rowDifList.pop(0)
            # row index in increasing order (top -> bottom)
            if increasing:
                lastRow, lastCol, keyList = tupGenColFixed(lastRow, lastCol, rowDif, keyList, increasing)
                increasing = False
            # row index in decreasing order (bottom -> top)
            else:
                lastRow, lastCol, keyList = tupGenColFixed(lastRow, lastCol, rowDif, keyList, increasing)
                increasing = True
            rowFixed = True
    return keyList


def tupGenRowFixed(lastRow, lastCol, colDif, keyList, increasing):
    '''
    lastRow: int, the last row index
    lastCol: int, the last columm index
    colDif: int, difference to be made
    keyList: list, of positions as keys
    increasing: bool

    return: lastRow, lastCol, keyList (modified)
    '''
    print 'lastRow =  ', lastRow, '  lastCol=  ', lastCol, '  colDif =  ', colDif
    for i in range(colDif):
        if increasing:
            keyList.append((lastRow, lastCol + 1 + i))

        else:
            keyList.append((lastRow, lastCol - 1 - i))
    if increasing:
        lastCol = lastCol + colDif
    else:
        lastCol = lastCol - colDif
    print keyList
    return lastRow, lastCol, keyList

def tupGenColFixed(lastRow, lastCol, rowDif, keyList, increasing):
    '''
    '''
    print 'lastRow =  ', lastRow, '  lastCol=  ', lastCol, '  rowDif =  ', rowDif
    for i in range(rowDif):
        if increasing:
            keyList.append((lastRow + 1 + i, lastCol))
        else:
            keyList.append((lastRow - 1 - i, lastCol))
    if increasing:
        lastRow = lastRow + rowDif
    else:
        lastRow = lastRow - rowDif
    print keyList
    return lastRow, lastCol, keyList

def intoDict(keyList):
    '''
    keyList: list, of positions as keys

    returns: dict, of positions as keys and numbers as values
    '''
    numDict = {}

    for i in range(len(keyList)):
        numDict[keyList[i]] = i

    return numDict

def printNum(numDict, row, col):
    '''
    numDict: dict
    row: int >= 1
    col: int>= 1

    return: prints the dictionary's values in a spiral fashion
    '''
    for i in range(row):
        print '  '.join([str(numDict[(i, j)]) for j in range(col)])












row = int(raw_input('row:  '))
col = int(raw_input('columm:  '))

spiralNumber(row, col)
