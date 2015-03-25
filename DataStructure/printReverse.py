# -*- coding: utf-8 -*-
# printReverse
def printReverse(data):
    '''
    data: .txt file

    returns: prints data in reverse
    '''
    line = data.readline() # data read until previous line
    # base case: end of file
    if line == '':
        return

    # recursive case:
    printReverse(data)
    print line,


data = open('printReverseTextFile.txt', 'r')
printReverse(data)
