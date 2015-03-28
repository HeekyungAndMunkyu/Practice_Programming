def oneOverSeries(n):
    '''
    n: int >= 1

    returns: float, sum of 1 + 1/2 + 1/3 + ... + 1/n
    '''
    # base case
    if n == 1:
        return 1.0
    # general case
    else:
        #print '1/%d' % n
        return 1.0/n + oneOverSeries(n-1)
