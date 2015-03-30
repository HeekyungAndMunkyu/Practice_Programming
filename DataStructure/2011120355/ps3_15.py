def calc(operand1, oper, operand2):
	'''
	operand1: float
	oper: a single string
	operand2: float

	return: float
	'''
	if oper == '+':
		return operand1 + operand2
	elif oper == '-':
		return operand1 - operand2
	elif oper == '*':
		return operand1 * operand2
	else:
		return operand1 / operand2

# create stack
stack = []
# read postfix expression, char by char
formula = raw_input("Input formula: ")

operand_making = ''

for token in formula:
	print 'token is', token
	# if not operator (== if operand)
	if token == ' ':
		if operand_making != '':
			stack.append(int(operand_making))
			operand_making = ''

	elif token not in '+-*/':
		operand_making += token
				
	# else	(== if operator)
	else:
		operand2 = stack.pop()
		operand1 = stack.pop()
		value = calc(operand1, token, operand2)
		stack.append(value)
	print stack
# the final result is in stack. pop it print it.
print "The result is: %d\n" % stack[0]

