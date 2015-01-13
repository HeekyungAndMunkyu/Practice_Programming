#find a sqaure root of an integer

x = int(raw_input('Enter an integer: '))
epsilon = 0.01
step = 0.1
guess = 0.0




#while guess is smaller than x
while guess <= x:
	if abs(guess**2 - x) >= epsilon:
		print guess, abs(guess**2 - x)
		guess += step

if abs(guess**2 - x) >= epsilon:
	print 'failed', guess

else:
	print 'succeeded: ', guess

