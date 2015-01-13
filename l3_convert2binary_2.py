#convert to binary_modified by me

num = int(raw_input('Enter an integer: '))
binary = ''
negative = False

#there are three cases: positive, zero, negative
#positive and negative can be computed in the same way except for the (+/-) sign

if num == 0:
	binary = '0'

#this is how we treat (+/-) sign problem.
if num < 0:
	num = abs(num)
	negative = True


#positive and negative are computed the same way.
while num >= 1: 
	binary = str(num%2) + binary
	num /= 2


#a final touch on the (+/-) sign
if negative:
	binary = '-' + binary



print 'The number typed in decimal is ' + binary + ' in binary.'
