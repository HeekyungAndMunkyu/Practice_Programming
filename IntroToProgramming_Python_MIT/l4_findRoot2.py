
def findRoot2(x, power, epsilon):
        '''
        abs(x) >= 1, power >= 1, epsilon > 0
        
        return: power root of x with epsilon error from x when powered
        '''

        #guess and check - generating guesses with bisection search


        high = max(x, 0.0)
        low = min(0.0, x)
        guess = 0.0

	if x < 0 and power%2 == 0:
		print 'it doesn\'t exist'
		return None

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
print findRoot2(x, power, epsilon)


