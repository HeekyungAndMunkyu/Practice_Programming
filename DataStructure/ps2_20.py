def printListReverse(lst):
    '''
    lst: list

    returns: prints the list in reverse order
    '''
    # base case
    if len(lst) == 1:
        print lst[-1]
    # general case
    else:
        print lst[-1],
        return printListReverse(lst[:-1])
