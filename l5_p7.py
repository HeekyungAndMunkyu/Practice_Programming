# l5_p7
# recursive fuction

def lenRecur(aStr):
	'''
	aStr: a string

	returns: int, the length of aStr
	'''
	
	if aStr == '':
		return 0

	elif aStr[0:] == aStr[0]:
		return 1

	else:	
		return 1 + lenRecur(aStr[1:])


aStr = raw_input('Enter a string:  ')

print 'The length of string ', aStr, '\' is', lenRecur(aStr) 
