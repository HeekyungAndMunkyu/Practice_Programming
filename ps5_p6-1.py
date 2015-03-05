# Problem set 5
# Problem 6-1


def swapsort(L):
    """ L: list, of int

        returns: list, sorted"""

    for i in range(len(L)):
#        for j in range(i+1, len(L)):
        for j in range(len(L)):
            print i, j
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
            print L
        print '--------------------'
    print 'final: ', L


L = [1, 2, 3, 4, 5]
swapsort(L)
