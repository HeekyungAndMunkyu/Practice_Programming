# L10 Hashing

from string import *




def hash(s):
    return string.ascii_lowercase.index(s[0])

print hash('dog')
print hash('key')
