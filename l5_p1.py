#l5 p1


def iterPower(base, exp):
	'''
	base: int or float
	exp: int >= 0
	
	returns: int or float, base^exp
	'''
	ans = 1
	
	if exp == 0:
		ans = 1	

	while exp > 0:
		ans *= base
		exp -= 1
	
	
	return ans

base, exp = raw_input('base, exp: ')

print iterPower(base, exp)
