# -*- coding: utf-8 -*-

# enable argv function
from sys import argv

script, filename = argv

# proceed or quit (deleting contents in file)
print "I'm trying to delete %r file." % filename
print "Type CTRL-C(^) to cancel." 
print "Press return to proceed."

raw_input("?")

# assign file to a variable 'target' with right to write
print "opening file ..."
target = open(filename, 'w')

# delete contents in the file with method 'trucate'
print "Delete file content. Bye!"
target.truncate()

print "Now, fill in the file line by line"

# assign content to be written
line1 = raw_input("first line: ")
line2 = raw_input("second line: ")
line3 = raw_input("third line: ")

print "Write these contents on file."

# wrtie the content previously written with method 'wrtie'
# format & escape string have been used. 
target.write('%s \n %s \n %s \n' % (line1, line2, line3))

# close the input stream after truncate & write
print "Finally, close the file."
target.close()
