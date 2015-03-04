# l6_p11


def biggest(aDict):
	'''
	aDict: dict, where all values are lists.
	
	returns: key, with the largest number of values associated with it
	'''
	
	# for each list in dictionaries
	for value in aDict.values():

		# if it is one of the lists with the maximum number of values
		if len(value) == len(max(aDict.values(), key = len)):
			

			# return the key associated with the list
			return aDict.keys()[aDict.values().index(value)]



	return None
