def findRoot1(x, power, epsilon):
	'''
	x >= 1, power >= 1, epsilon > 0
	
	return: power root of x with epsilon error from x when powered
	'''

	#guess and check - generating guesses with bisection search
	

	high = x
	low = 0.0
	guess = 0.0



	while abs(guess**power - x) > epsilon:
		guess = (high + low)/2
		print 'guess =', guess
		if guess**power > x:
			high = guess
		else:
			low = guess
	if abs(guess**power - x) > epsilon:
		return None
	else:
		return 'power root of x is ', guess



x = float(raw_input('x = '))
power = float(raw_input('power = '))
epsilon = float(raw_input('epsilon = '))
print findRoot1(x, power, epsilon)

