



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

	if substr[-1] <= s[len(substr)]:
		substr = substr + s[len(substr)]

	return substr


s = raw_input('enter a string: ')



longest = alphastr(s)

print 'first longest:', longest

while len(s) > len(longest):
	s = s[len(longest):]
	longestChallenger = alphastr(s)


	print 'longest:', longest, 'challenger:', longestChallenger	
	if len(longest) < len(longestChallenger):
		longest = longestChallenger

print 'Longest substring in alphabetical order is:', longest
	
