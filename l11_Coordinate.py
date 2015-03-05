import math

class Coordinate(object):
    def __init__(self, x, y):

        self.x = x
        self.y = y


    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


c = Coordinate(3, 4)
other = Coordinate(0, 0)

print 'print c'
print c
print
print 'distance'
print c.distance(other)
print 'type(c)'
print type(c)
print 'Coordinate'
print Coordinate
