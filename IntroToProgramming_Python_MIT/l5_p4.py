#l5_p4

def gcdIter(a, b):
	'''
	a, b : int > 0

	return: int, greatest common divisor
	'''


	gcd = min(a, b)

	while gcd > 1:
		if a % gcd == 0 and b % gcd == 0:
			return gcd
		gcd -= 1
	
	return gcd
