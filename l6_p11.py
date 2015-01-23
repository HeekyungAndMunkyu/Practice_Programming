# l6_p11

aDict = {'c': [10, 6, 6, 4, 17], 'e': [6, 18], 'h': [4, 20, 1, 19], 'M': [], 'S': [8, 0, 17, 19], 's': [15], 't': [], 'V': [], 'z': [3, 8, 3]}

def biggest(aDict):
	'''
	aDict: dict, where all values are lists.
	
	returns: key, with the largest number of values associated with it
	'''

	for value in aDict.values():
		if len(value) == len(max(aDict.values(), key = len):
			return aDict.keys()[aDict.values().index(value)]
		else:
			return None




print biggest(aDict)
