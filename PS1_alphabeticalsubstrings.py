#find the longest substring of s in which the letters occur in alphabetical order



def alphaSubstr(str):
	'''str = a string
	
	returns the first alphabetical order substring.
	'''
	
	substr = ''
	whereisfinalword = 0

	for i in range(len(str)-1):
		whereisfinalword += 1
		if str[i] <= str[i+1]:
			substr += str[i]
			print substr
		else:
			if i == len(str)-2:
				break	
	
	if len(substr) == 0:
		return str[0]
	else:
		substr = substr + str[whereisfinalword]
		breakpoint = 0
		for i in range(len(substr)-1):
			breakpoint += 1
			if str[i] > str[i+1]:
				break
			else:
				return substr
		return substr[:breakpoint]

str = raw_input('any lower case only string: ')

string = alphaSubstr(str)

print string 





def alphaSubstr2(str):
	'''
	str = a string
        
        returns the first alphabetical order substring.
        '''

	substr = ''
	startpoint = -1
	endpoint = 0
	
	if str[0] > str[1]:
		for i in range(len(str)-1):
			startpoint += 1
			print startpoint
			while str[i] > str[i+1]:
				break
	
		str = str[startpoint:]
		print 'after slicing: ', str
	

	for t in range(len(str)-1):
		print str	
		substr = substr + str[t]
		if str[t] > str[t+1]:
			break

	return substr




str = raw_input('any lower case only string: ')

string = alphaSubstr2(str)

print 'answer = ', string

