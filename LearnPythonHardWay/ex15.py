# -*- coding: utf-8 -*-

# enable 'argv' function
from sys import argv

script, filename = argv

# open a file and assign it to txt
txt = open(filename)

print "Content of the file %r:" % filename

# read() returns a string
# print prints the string
print txt.read()

txt.close()



