#l5
#recursion on non numeric values
#palinderoms


def isPal(s):
	'''
	s: str (any sentence)

	returns: bool (True if Palindrom or False if not)
	'''

	ss = s.lower()
	sss = ''
	
	for i in ss:
		if i in 'abcdefghijklmnopqrstuvwxyz':
			sss = sss + i
	
	if len(sss) == 2 or len(sss) == 1:
		if sss[0] == sss[-1]:
			return True
	
		else:
			return False	

	else:
		return sss[0] == ss[-1] and isPal(sss[1:-1])



s = raw_input('enter a string to test for palindrome:  ')

print isPal(s)

