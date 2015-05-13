import numpy as np

print "Make a 3 row x 4 column array of random numbers"
x = np.random.random((3, 4))
print x
print

print "Add 1 to every element"
x = x + 1
print x
print

print "Get the element at row 1, column 2"
print x[1, 2]
print

# The colon syntax is called "slicing" the array.
print "Get the first row"
print x[0, :]
print

print "Get every 2nd column of the first row"
print x[0, ::2]
print
