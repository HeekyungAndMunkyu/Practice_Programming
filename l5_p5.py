#l5_p5

def gcdRecur(a, b):
	'''
	a, b: positive integers
	
	returns: a positive integer, the greatest commin divisor of a & b.
	'''

	if b == 0:
		return a

#	return gcd(a % b, b) 
	return gcdRecur(b, a % b)
