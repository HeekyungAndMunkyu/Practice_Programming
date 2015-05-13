# peak finder

def peakFinder(listOfFloats):
    '''
    listOfFloats: list, of floats

    returns: float (a peak if it exists)
    '''

    middleIndex = len(listOfFloats)/2
    middleNum = listOfFloats[middleIndex]
    print 'from the list', listOfFloats, ',', middleNum, 'at index', middleIndex

    if len(listOfFloats) == 1:
        print middleNum, 'at index', middleIndex
    if middleNum <= listOfFloats[middleIndex - 1]:
        return peakFinder(listOfFloats[:middleIndex])

    elif middleNum <= listOfFloats[middleIndex + 1]:
        return peakFinder(listOfFloats[middleIndex + 1:])

    else:
        print middleNum, 'at index', middleIndex
