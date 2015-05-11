# l5_p9
# iterative function


#def semordnilap(str1, str2):
#	'''
#	str 1: a string
#	str 2: a string

#	returns: True if str 1 and str2 are smordnilap:
#		False otherwise.
#	'''

#	str1backwards = ''

#	for i in str1:
#		str1backwards = i + str1backwards

#	return str1backwards == str2



# recursive function
def semordnilap(str1, str2):
	'''
	str1, str2: str

	returns: True if semordnilap; False otherwise.
	'''
	if len(str1) != len(str2):
		return False

	if len(str1) == 2:
		return str1[0] == str2[-1] and str1[-1] == str2[0]

	else:
		return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1]) 



def semordnilapWrapper(str1, str2):
	# a single-length string cannot be semordnilap
	if len(str1) == 1 or len(str2) == 1:
		return False

	# Equal strings cannot be semordnilap
	if str1 == str2:
		return False

	return semordnilap(str1, str2)


str1 = raw_input('string 1:  ')
str2 = raw_input('string 2:  ')

print semordnilapWrapper(str1, str2)
