



def alphastr(s):
	'''when enters a string

	returns the first alphabetical order substring
	'''

	startingPoint = 0
	endPoint = -1
	substr = ''

	#find the starting point
	for i in range(len(s) - 1):

		if s[i] <= s[i+1]:
			startingPoint = i
			break

	s = s[startingPoint:]



	#find the end point
	for t in range(len(s) - 1):
		substr = substr + s[t]
		if s[t] > s[t+1]:
			endPoint = t
			break
		else:
			endPoint = t + 1

	if substr[-1] <= s[len(substr)]:
		substr = substr + s[len(substr)]

#	return substr
	return endPoint

s = raw_input('enter a string: ')



#longest, endPoint = alphastr(s)
longestChallenger = ''

print alphastr(s)
print 'first longest:', longest, 'endPoint:', endPoint, type(endPoint)

while len(s) > len(longest):


	# slicing s to find the next longest challneger
	if longest in s:

		s = s[endPoint + 1:]

	print 's =', s
	longestChallenger, endPoint = alphastr(s)

        print 'longest:', longest, 'challenger:', longestChallenger

	if len(longest) < len(longestChallenger):
		longest = longestChallenger



print 'Longest substring in alphabetical order is:', longest
	
