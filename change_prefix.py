from sys import argv
import os

'''
    How to use this script?

    >$python change_prefix.py [before_prefix] [after refix]

    And Here is sample scenario

    $ ls ~/Workspace/python
        ex_12.py ex_24.py
    $ python change_prefix.py ex example
    > ~/Workspace/python/
    $ ls ~/Workspace/python
        example_12.py example_24.py
'''

script, before_prefix, after_prefix = argv

path = raw_input(">")

for filename in os.listdir(path):
    if filename.startswith(before_prefix):
        src = path + filename
        filename = filename[len(before_prefix):]
        dst = path + after_prefix + filename

        os.rename(src, dst)
