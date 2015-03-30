# palindrome

import string

def isPalindrome(sentence):
	'''
	sentence: str
		print sentence
		print sentence reversed
	return: True if palindrome; False otherwise
	'''
	stack = []
	for c in sentence:
		if c in string.ascii_letters:
			stack.append(c.lower())
	original_sentence = ''.join(stack)
	print 'The sentence without uppercase and punctuations: ' + original_sentence
	
	reversed_sentence = ''
	while stack != []:
		reversed_sentence += stack.pop()
	print 'The reversed sentece: ' + reversed_sentence

	if original_sentence == reversed_sentence:
		return True
	return False

sentence = raw_input('Type a sentence to test for palindrome: ')
result = isPalindrome(sentence)
if result == True:
	print '\"%s\" is palindrome.' % sentence
else:
	print '\"%s\" is NOT palindrome.' % sentence
