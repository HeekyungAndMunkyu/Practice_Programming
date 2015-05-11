class intSet(object):
    def __init__(self):
        self.set = []

    def __str__(self):
        return '{' + ','.join([str(e) for e in self.set]) + '}'

    def insert(self, e):
        if e not in self.set:
            self.set.append(e)

    def member(self, e):
        return e in self.set

    def remove(self, e):
        if e in self.set:
            self.set.remove(e)
    def intersect(self, other):
        intersectSet = []
        for i in self.set:
            if i in other.set:
                intersectSet.append(i)
        if intersectSet == []:
            return 'There is no common item.'
        return intersectSet

    def len(s):
        return len(s.set)
