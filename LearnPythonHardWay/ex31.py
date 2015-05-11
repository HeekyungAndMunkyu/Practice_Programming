# -*- coding: utf-8 -*-

print "You've just entered a dark room with two doors.",
print "Which room would you enter, the first one or the second one?"

door = raw_input(">")

if door == "1":
    print "The big bear is having cheesecake. What are you going to do?"
    print "1. Take away the cheesecake."
    print "2. Yell at the bear."

    bear = raw_input(">")

    if bear == "1":
        print "The bear eats up your head. Well done!"
    elif bear == "2":
        print "The bear eats up your legs. Well done!"
    else:
        print "Um, maybe doing %s was better. The bear is running away." % bear

elif door == "2":
    print "Take a look at the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input(">")

    if insanity == "1" or insanity == "2":
        print "Your body survives with the power of jelly pudding. Well done!"
    else:
        print "Insanity makes your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on knife and die. Good job!"
