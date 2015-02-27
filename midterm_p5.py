def laceStrings(s1, s2):
    '''
    s1, s2: str   (len(str)>= 0)

    returns: str, with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    '''
    newStr = ''

    maxStr = s1
    minStr = s2

    if len(maxStr) < len(s2):
        maxStr = s2
        minStr = s1

    for i in range(len(minStr)):
        newStr += s1[i] + s2[i]

    for i in range(len(minStr), len(maxStr)):
        newStr += maxStr[i]
    return newStr

s1 = raw_input('string 1: ')
s2 = raw_input('string 2: ')

print laceStrings(s1, s2)
