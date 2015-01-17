#Counting 'bob's
#s = a string of lower case characters
#s will be handled by instructers. 

#s = raw_input('Enter any word only comprised of lower case characters: ')

numofBobs = 0

while 'bob' in s:
	numofBobs += 1
	i = s.index('bob')
	s = s[i+1:]

print 'Number of times bob occurs is:', numofBobs
	
