# L9 Exponential Complexity

def getSubsets(L):
    global recur_call
    recur_call += 1
    print '<',recur_call,'>', 'recur in'
    res = []
    if len(L) == 0:
        print '<break> recur out'
        return [[]]

    smaller = getSubsets(L[:-1]) # list
    print 'smaller is', smaller
    extra = L[-1:] # list
    print 'extra is', extra

    new = []
    for small in smaller:
        new.append(small + extra) # list + list
    print 'smaller + new', smaller + new
    print '<',recur_call,'>', 'recur out'
    return smaller + new # list + list

recur_call = 0
A = [1,2,3]
print 'A'
print getSubsets(A)
print
