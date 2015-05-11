# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'mandarin', 'pear', 'apricot']
change = [1, '10KRW', 2, '100KRW', 3, '500KRW']

# the first for-statement iterates over the list
for number in the_count:
    print "This number is %d." % number

# Same as above
for fruit in fruits:
    print "Fruit type: %s" % fruit

# iterates over the mixed list
for i in change:
    print "Recieved change: %s" % i

# You could also make a list. Start with an empty list.
elements = []

# and use a range function counts o to 5
for i in range(0, 6):
    print "Add %d to the list." % i
    #append is a function for list
    elements.append(i)

elements = []

elements = elements + range(0, 6)

# You can also print them
for i in elements:
    print "element is %d" % i
