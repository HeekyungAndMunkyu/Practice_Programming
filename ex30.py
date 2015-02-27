# -*- coding: utf-8 -*-

people = 30
cars = 40
buses = 15


if cars > people:
    print "I need to ride on a car."
elif cars < people:
    print "I should not ride on a car."
else:
    print "I can't decide."

if buses > cars:
    print "There are too many buses."
elif buses < cars:
    print "I can take buses as well."
else:
    print "Still, I can't decide."

if people > buses:
    print "Right. Let's take the buses."
else:
    print "Right. Let's stay home."
