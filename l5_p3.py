#l5_p3

def recurPowerNew(base, exp):
	'''
	base: float or int
	exp: int >= 0
	
	return: int or float, base^exp
	'''

	if exp == 0: 
		return 1

	elif exp % 2 == 0:
		return recurPowerNew(base, exp / 2) * recurPowerNew(base, exp / 2)

	else:
		return base * recurPowerNew(base, exp - 1)
