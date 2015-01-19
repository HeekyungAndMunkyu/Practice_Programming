# -*- coding: utf-8 -*-

# a function similar to the script of argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# Good. In fact, *args is not necessary. Let's do this way.
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# Now, this function receives only one argument.
def print_one(arg1):
	print "arg1: %r" % arg1

# Now, this function receives no argument.
def print_none():
	print "Receives nothing."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
	
