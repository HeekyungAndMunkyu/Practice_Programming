# -*- coding: utf-8 -*-

people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is going to end."

if people > cats:
    print "Not too many cats. The world is not going to an end."

if people < dogs:
    print "The world is going to be flooded with dog saliva."

if people > dogs:
    print "The world would stay dry."


dogs += 5

if people >= dogs:
    print "People are more than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."
