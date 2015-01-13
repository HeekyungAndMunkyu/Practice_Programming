#find a square root of an integer

x = int(raw_input('Enter an integer: '))
epsilon = 0.01
step = 0.1
guess = 0.0


#while the guess is not close enough to answer
while abs(guess**2 - x) >= epsilon:
	if guess <= x:
		print guess, abs(guess**2 - x)
		guess += step
	else:
		print 'break', guess
		break

if abs(guess**2- x) >= epsilon:
	print 'failed'

else:
	print 'succeeded:',guess
