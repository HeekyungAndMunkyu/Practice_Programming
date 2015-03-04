





def square (x):
	return x * x

def twoPower (x, n):
	while n > 1:
		print 'x = ', x, 'n= ', n
		x = square (x)
		n = n/2
	return x

x = int(raw_input('enter an integer: '))
n = int(raw_input('enter power: '))

print twoPower(x, n)
