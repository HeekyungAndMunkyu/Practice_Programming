# l5_p8
# recursive function

def isIn(char, aStr):
	'''
	char: a single character
	aStr: an alphabetized string

	returns: Ture if char is in aStr; False otherwise
	'''
	if aStr == '':
		return False

	if aStr == char:
		return True

	if aStr[len(aStr)/2] == char:
		return True

	elif aStr[len(aStr)/2] > char:
		return isIn(char, aStr[:len(aStr)/2])

	else:
		return isIn(char, aStr[len(aStr)/2 + 1:])




char = raw_input('char:  ')
aStr = raw_input('aStr:  ')

print isIn(char, aStr)
