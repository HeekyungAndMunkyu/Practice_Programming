def isVowel2(char):

	'''
	char: a single letter of any case

	returns: True if char is a vowel and False otherwise.
	'''

	#my code
	
	vowel = False
	
	while not vowel:
		for i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
			if char == i:
				return True 



char = raw_input ( 'Enter any single string (uppercase or lowercase): ')

print isVowel2(char)

#sample code 1
def isVowel2_s1(char):
	if char in 'aeiouAEIOU':
		return True
	else:
		return False





#sample code 2
def isVowel2_s2(char):
	return char.lower() in 'aeiou'
