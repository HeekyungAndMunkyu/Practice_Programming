# sprialnumber

def sprialNumber(row, col):
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
    # make a dictionary of numbers as values (int) and position as keys (tuple)
    # ex) {(0,0): '0', (0,1): '1'}

    # print the dictionary in a sprial fashion
    printSpiral(intoDict(row, col))

def intoDict(row, col):
    '''
    row: int >= 1, row
    col: int >= 1, columm

    return: dict, keys = positions in tuple, values = numbers in int
        ex)
        row = 3, col = 1
        {(0,0): '0', (0,1): '1', (0,2): '2'}
    '''
    # number variable
    num = 0
    numDict = {}

    rowListFixed = range(0, row)
    colListFixed = range(0, col)
    print 'rowListFixed = ', rowListFixed, 'colListFixed = ', colListFixed

    rowListMoving = range(row - 1, -1, -1)
    colListMoving = range(col, -1, -1)
    print 'rowListMoving = ', rowListMoving, 'colListMoving = ', colListMoving

    # make position keys with tuples
    rowPositionFixed = True
    rowTopSide = True
    colRightSide = True
    leftToRight = True # row
    topToBottom = True # columm

    while num <= row * col - 1:

        # when row position is fixed and only columm position is changing
        if rowPositionFixed == True:
            print 'rowPosition Fixed'
            if rowTopSide == True:
                rowPosition = rowListFixed.pop(0)
                colPosition = colListMoving.pop(0)
                print 'row TopSide', rowPosition, colPosition

                # left -> right
                if leftToRight == True:
                    num, numDict = tupGenRowFixed(rowPosition, colPosition, num, numDict)
                    leftToRight = False
                # right -> left
                else:
                    num, numDict = tupGenRowFixedReversed(rowPosition, colPosition, num, numDict)
                    leftToRight = True
                rowTopSide = False
            else:
                rowPosition = rowListFixed.pop(-1)
                colPosition = colListMoving.pop(0)
                print 'row DownSide', rowPosition, colPosition
                num, numDict = tupGenRowFixed(rowPosition, colPosition, num, numDict)
                rowTopSide = True
            rowPositionFixed = False # switch mode
        # when x's position is fixed and only y's position is changing
        else:
            print 'colPosition Fixed'
            if colRightSide == True:
                colPosition = colListFixed.pop(-1)
                rowPosition = rowListMoving.pop(0)
                print 'col RightSide', rowPosition, colPosition
                num, numDict = tupGenColFixed(rowPosition, colPosition, num, numDict)
                colRightSide = False
            else:
                colPosition = colListFixed.pop(0)
                rowPosition = rowListMoving.pop(0)
                print 'col LeftSide', rowPosition, colPosition
                num, numDict = tupGenColFixed(rowPosition, colPosition, num, numDict)
                colRightSide = True
            rowPositionFixed = True
    return numDict, 'total number =', len(numDict)

def tupGenRowFixed(rowPosition, colPosition, num, numDict):
    '''
    '''

    for i in range(0, colPosition):
        numDict[(rowPosition, i)] = num
        print numDict
        num += 1
    return num, numDict

def tupGenRowFixedReversed(rowPosition, colPosition, num, numDict):
    '''
    '''

    for i in range(colPosition, 0, -1):
        numDict[(rowPosition, i)] = num
        print numDict
        num += 1
    return num, numDict

def tupGenColFixed(rowPosition, colPosition, num, numDict):
    '''
    '''

    for i in range(0, rowPosition):
        numDict[(i,colPosition)] = num
        print numDict
        num += 1
    return num, numDict

def printSprial(numDict):
    '''
    numDict: dict, of numbers with position as keys

    return: prints numbers in a specified position
    '''



row = int(raw_input('row:  '))
col = int(raw_input('columm:  '))

print intoDict(row, col)
#printSpiral(intoDict(row, col))
