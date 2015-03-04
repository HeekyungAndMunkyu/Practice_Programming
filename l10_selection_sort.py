# L10 Selection Sort

def selSort(L):
    '''
    L: list, of integers
        for each element in the list, switch the value with the smallest among
        those with bigger indices
    returns: list, sorted
    '''

    # for each element in the list (except the last one)
    for i in range(len(L)-1):
        minIndx = i
        minVal = L[i]
        j = i + 1    # next element index

        # find the smallest among those with bigger indices (i < j < len(L))
        while j < len(L):    # not only smaller but 'smallest'
            print j
            if L[j] < minVal:
                minIndx = j
                minVal = L[j]
            j += 1
        print
        print 'L[i] = %d     L[minIndx] = %d' % (L[i], minVal)
        print

        # switch the value with the smallest found
        L[minIndx] = L[i]
        L[i] = minVal

        print L
        print

    print 'Sorted List', L

A = [2, 5, 6, 7, 3, 1, 4]
print 'Let\'s sort this list: ', A
print
selSort(A)
