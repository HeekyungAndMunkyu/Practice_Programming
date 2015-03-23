def intToBinaryStr(n):
    '''
    n: int, decimal

    returns: str, binary
    '''
    # base case
    if n == 0 or n == 1:
        return str(n)

    # general case
    else:
        return intToBinaryStr(n / 2) + str(n % 2)
