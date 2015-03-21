# -*- coding: utf-8 -*-
# printReverse
def printReverse(data):
    '''
    data: .txt file

    returns: prints data in reverse
    '''
    # base case: end of file
    print type(data), data
    if not data.readline():
        return

    # recursive case:
    line = data.readline() # data read until previous line
    printReverse(line)
    print line,


data = open('printReverseTextFile.txt', 'r')
print type(data)
printReverse(data)
