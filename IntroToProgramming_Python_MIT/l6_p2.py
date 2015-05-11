# l6_p2

def oddTuples(aTup):
	'''
	aTup: a tuple

	returns: tuple, every other element of aTup
	'''

	return aTup[::2]

aTup = tuple(raw_input('a tuple: '))
print aTup
print type(aTup) 
print oddTuples(aTup)

