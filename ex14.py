# -*- coding: utf-8 -*-

from sys import argv

script, user_name = argv
prompt = 'you answer:'

print "Hi, %s. I am %s script." % (user_name, script)
print "I'll ask you a few questions."
print "%s, do you love me?" % user_name
likes = raw_input(prompt)

print "%s, where do you live?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you own?"
computer = raw_input(prompt)

print """
Well, you replied '%s' when asked if you loved me.
You live in '%s', though I don't know where it is.
And you own '%s' computer. Cool.
""" % (likes, lives, computer)


