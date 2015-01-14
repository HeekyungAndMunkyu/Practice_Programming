#Find a square root of an integer using bisection search
#my code


x = int(raw_input('Enter an integer: '))
guess = 0.0
epsilon = 0.01
minimum = 0.0
maximum = x



while abs(guess**2 - x) > epsilon:
	if guess**2 - x > 0:
		maximum = min(guess, maximum)
		print guess, guess**2 - x, 'too big', minimum, maximum
	elif guess**2 - x < 0:
		minimum = max(minimum, guess)
		print guess, guess**2 - x,'too small', minimum, maximum
	guess = (minimum + maximum)/2 		   

print 'The square root of ', x, ' is ', guess, '.'



#sample code
print ''
print 'sample code'
x = int(raw_input('Enter an integer: '))
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
	print 'low= ', low, 'high= ', high, 'ans= ', ans
	numGuesses += 1
	if ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (high + low)/2.0

print 'numGuesses= ', numGuesses
print ans, ' is close enough to square root of ', x 


