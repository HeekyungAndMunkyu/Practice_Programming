def printLove():
    print "Love"

print
print 'without print'
printLove()

print
print 'with print'
print printLove()

print 
print 'assign'
t = printLove()
print t
print type(printLove)
print type(printLove())
