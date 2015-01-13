#convert to binary _ different version

num = int(raw_input('Enter an integer: '))

binary = ''
negative = False


if num == 0:
	binary = '0'

if num < 0:
	num = abs(num)
	negative = True

while num >= 1: 
	binary = str(num%2) + binary
	num /= 2

if negative:
	binary = '-' + binary



print 'The number typed in decimal is ' + binary + ' in binary.'
