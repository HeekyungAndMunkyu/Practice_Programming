def McNuggets(n):
    '''
    n: int>= 0

    return: bool, True if some integer combination of 6, 9 and 20 equals n.
        False, otherwise.
    '''
    n = int(n)
    a = 0
    b = 0
    c = 0

    # generate a, b, c
    # a + b + c = abc
    abc = 0
    while 6*a + 9*b + 20*c < n:
#        print 6*a + 9*b + 20*c, '<', n
        for i in range(abc + 1):
            a = i
            for j in range(abc - a + 1):
                b = j
                c = abc - a - b
#                print 'a b c', a, b, c, '6a + 9b + 20c', 6*a + 9*b + 20*c
                if 6*a + 9*b + 20*c == n:
                    return True

        abc += 1

    return False

n = raw_input('n: ')

print McNuggets(n)
