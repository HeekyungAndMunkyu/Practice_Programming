# -*- coding: utf-8 -*-

print "Let's practice everything."
print "You should know about escape sequence for inserting \n new lines or \t tab using \\."

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "---------------"
print poem
print "---------------"


five = 10 - 2 + 3 - 6
print "The result should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates



start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "starting point: %d" % start_point
print "There are %d benas, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "You can do it the other way."
print "There are %d benas, %d jars, and %d crates." % secret_formula(start_point) 
