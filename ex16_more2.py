# write a program to read what's written on 'ex15_sample.txt' after ex16.py modification

from sys import argv

script, filename = argv

txt = open(filename)

print txt.read()
