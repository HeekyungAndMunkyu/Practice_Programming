# -*- coding: utf-8 -*-

from sys import exit

def gold_room():
    '''
    returns: choices you get from entering the gold room
    '''
    print "This is a room full of gold. How much do you want?"

    next = raw_input('>')

    # the first question
    # if 0 or 1 included, go to the next question
    if "0" in next or "1" in next:
        how_much = int(next)
    # if not, you're dead.
    else:
        dead("Man, first learn how to count.")

    # the second question
    if how_much < 50:
        print "Good, you are not greedy. You won!"
        exit(0)
    else:
        dead("What a greedy person!")


def bear_room():
    '''
    returns: choices you get from entrering the bear room.
    '''
    print "Here is one bear."
    print "The bear has a huge amount of honey."
    print "A fat bear is in front of the other door."
    # question
    print "How are you going to move the bear?"
    bear_moved = False

    # keep getting the response until dead or exited
    while True:
        next = raw_input(">")

        if next == "steal honey":
            dead("The bear looks at you and slaps your cheeck off.")

        # first time teasing
        elif next == "tease the bear" and not bear_moved:
            print "The bear moved away from the door. Now, you can exit."
            bear_moved = True
        # not-first-time teasing -> you're dead
        elif next == "tease the bear" and bear_moved:
            dead("The bear chews your legs off out of anger.")

        # after the first time teasing, you can open the door to the gold room.
        elif next == "open the door" and bear_moved:
            gold_room()

        # back to the question
        else:
            print "Don't understand what you're saying."


def cthulhu_room():
    '''
    returns: choices you get from entering the cthulhu room.
    '''

    print "Here you see the evil, Cthulhu."
    print "He, no, that thing, or whatever looks at you and you go crazy"
    # question
    print "Are you going to run away or eat your head off?"

    next = raw_input(">")

    # if run away, go back to the start
    if "run away" in next:
        start()
    # if eat, you're dead.
    elif "eat" in next:
        dead("Um, tasty!")
    # or, go back to cthulhu room
    else:
        cthulhu_room()



def dead(why):
    '''
    returns: game over with you dead
    '''

    print why, "Good job!"
    exit(0)

def start():
    '''
    returns: game start
    '''

    print "You are in a dark room."
    print "There are doors on your right and left side."
    # question
    print "Which door do you choose?"

    next = raw_input(">")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You went dead while wandering around the door")


# actual script starts here
start()
