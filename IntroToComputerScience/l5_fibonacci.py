#l5
#recursion with multiple base cases

def fibona(n):
	'''
	n: int >= 1 (number of months)

	returns: int (number of rabbits)
	'''
	if n == 1:
		return 1

	elif n == 2:
		return 2	
	else:
		return fibona(n-1) + fibona(n-2)


n = int(raw_input('How many months?'))

print 'There are', fibona(n), 'rabbits.'
