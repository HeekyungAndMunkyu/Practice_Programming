# l6
# Tuples

def findDivisors(n1, n2):
	'''
	n1, n2: positive integers (int >= 1)

	returns: a tuple containing common divisors of n1 & n2
	'''

	cd = max(n1, n2)
	cdTup = ()
	while cd >= 1:
		if n1 % cd == 0 and n2 % cd == 0:
			cdTupNew = (cd,)
			cdTup = cdTup + cdTupNew
		cd -= 1
	return cdTup



n1 = int(raw_input('n1: '))
n2 = int(raw_input('n2: '))

print findDivisors(n1, n2)
			
