# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv

def print_all(f):
	'''
	enters a filename

	returns the file content as a string and prints them.
	'''

	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	'''
	enters a number & a filename

	returns the file content on the line number entered.
	'''
	print line_count, f.readline()

current_file = open(input_file)

print "Let's print the entire file.\n"

print_all(current_file)

print "This time, let's rewind the file like a cassette tape."

rewind(current_file)

print "Let's print out three lines."

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
