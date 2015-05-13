# A program that takes the dimensions of an MxN array,
# and fills it with a sequence in the spiral fashion.

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
    # 1 make a tuple list
    # 2 make the tuple list into dictionary with number values assigned
    # 3 print out the dictionary in a spiral fashion
    printNum(intoDict(intoTuple(row, col)), row, col)



def intoTuple(row, col):
    '''
    row: int >= 1, row
    col: int >= 1, columm

        the index tuple changes in a way that only one of the index is changing
        while the other is fixed (for example, while row index is fixed, only
        columm index changes)

        when generating tuples of index, tuples sharing the fixed index, either
        row or columm, are generated together within the same function. When
        visualized, those tuple groups consitute rows and columms.

    return: a tuple, of positions as keys
        len(intoTupe(row, col)) = row * col

        ex)
        row = 1, col = 3
        [(0,0), (0,1), (0,2)]
    '''

    # into the biggest index numbers
    rowIndex = row - 1
    colIndex = col - 1

    # result
    keyList = []

    # last position index
    lastRow = 0
    lastCol = -1    # adjusted for first time call to tupGenRowFixed

    # difference to be added while one of the index is fixed
    rowDifList = range(rowIndex, -1, -1)
    colDifList = range(colIndex + 1, -1, -1)
    rowDif = 0
    colDif = 0

    # branching variables
    rowFixed = True # False: columm fixed
    increasing = True # False: decreasing

    print
    print 'rowDifList:', rowDifList, '       colDifList:', colDifList

    while len(keyList) < row * col:
        print

        # when row index is fixed
        if rowFixed:
            print 'rowFixed'
            colDif = colDifList.pop(0)
            # columm index in increasing order (left -> right)
            if increasing:
                lastRow, lastCol, keyList = tupGenRowFixed(lastRow, lastCol,
                colDif, keyList, increasing)
            # columm index in decreasing order (right -> left)
            else:
                lastRow, lastCol, keyList = tupGenRowFixed(lastRow, lastCol,
                colDif, keyList, increasing)
            rowFixed = False
        # when columm index is fixed
        else:
            print 'colFixed'
            rowDif = rowDifList.pop(0)
            # row index in increasing order (top -> bottom)
            if increasing:
                lastRow, lastCol, keyList = tupGenColFixed(lastRow, lastCol,
                rowDif, keyList, increasing)
                increasing = False
            # row index in decreasing order (bottom -> top)
            else:
                lastRow, lastCol, keyList = tupGenColFixed(lastRow, lastCol,
                rowDif, keyList, increasing)
                increasing = True
            rowFixed = True

        print

    return keyList


def tupGenRowFixed(lastRow, lastCol, colDif, keyList, increasing):
    '''
    lastRow: int, the last tuple's row index
    lastCol: int, the last tuple's columm index
    colDif: int, difference to be added or subtracted
    keyList: list, of positions as keys
    increasing: bool

        This function appends a row of tuples with the same row index

    return: lastRow, lastCol, keyList
        lastRow: lastRow
        lastCol: lastCol +/- colDif
        keyList: a row of tuples with the same row index appended
    '''
    print
    print 'lastRow =  ', lastRow, '  lastCol=  ', lastCol, '  colDif =  ', colDif
    print

    for i in range(colDif):
        if increasing:
            keyList.append((lastRow, lastCol + 1 + i))

        else:
            keyList.append((lastRow, lastCol - 1 - i))
    if increasing:
        lastCol = lastCol + colDif
    else:
        lastCol = lastCol - colDif

    print
    print keyList
    print

    return lastRow, lastCol, keyList


def tupGenColFixed(lastRow, lastCol, rowDif, keyList, increasing):
    '''
    lastRow: int, the last tuple's row index
    lastCol: int, the last tuple's columm index
    rowDif: int, difference to be added or subtracted
    keyList: list, of positions as keys
    increasing: bool

        This function appends a columm of tuples with the same columm index

    return: lastRow, lastCol, keyList
        lastRow: lastRow +/- rowDif
        lastCol: lastCol
        keyList: a columm of tuples with the same row index appended
    '''
    print
    print 'lastRow =  ', lastRow, '  lastCol=  ', lastCol, '  rowDif =  ', rowDif
    print

    for i in range(rowDif):
        if increasing:
            keyList.append((lastRow + 1 + i, lastCol))
        else:
            keyList.append((lastRow - 1 - i, lastCol))
    if increasing:
        lastRow = lastRow + rowDif
    else:
        lastRow = lastRow - rowDif

    print
    print keyList
    print

    return lastRow, lastCol, keyList


def intoDict(keyList):
    '''
    keyList: list, of positions as keys

    returns: dict, of positions as keys and numbers as values
        ex)
        row = 3, col = 1
        {(0,0): '0', (0,1): '1', (0,2): '2'}

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

    print '<<< THE ANSWER >>>'
    for i in range(row):
        print '  '.join([str(numDict[(i, j)]) for j in range(col)])












row, col = [int(i) for i in raw_input('Please enter two integers (>= 1) separated\
 by a whitespace (row columm):').split()]

spiralNumber(row, col)
