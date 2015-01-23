# l6_p10

def howMany(aDict):
	'''
	aDict: A dictionary, where all the values are lists.

	returns: int, how many values are in the dictionary.
	'''
	

	length = 0
	
	for lst in aDict.value():
		length += len(lst)
		print len(lst)
	return length



