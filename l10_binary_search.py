# L10 Search Algorithms

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


e = 3
A = [3, 5]
B = [5, 3]
C = [2, 2]

print 'A', search(A, e)
print 'B', search(B, e)
print 'C', search(C, e)
