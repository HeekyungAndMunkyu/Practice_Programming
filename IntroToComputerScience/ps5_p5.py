# Problem Set 5
# Problem 5


def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-1-i] == e:
            return True
        if L[i] < e:
            return False
    return False


L = []
e = 1
print search(L, e)
print newsearch(L, e)
