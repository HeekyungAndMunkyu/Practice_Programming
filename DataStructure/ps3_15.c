#include <stdio.h>
#include <stdlib.h>
#include "stackADT.h"

// prototype declarations
bool isOperator (char token);
int calc (int operand1, int oper, int operand2);

int main (void)
{
// local definitions
	char token;
	int operand1;
	int operand2;
	int value;
	int* dataPtr;
	STACK* stack;

// statements
	// create stack
	stack = createStack ();

	// read postfix expression, char by char
	printf ("Input formula: ");
	while ((token = getchar ()) != '\n')
		{
				 
		if (!isOperator (token))
			{
			dataPtr = (int*) malloc (sizeof (int));
			*dataPtr = atoi (&token);
			pushStack (stack, dataPtr);
			}	// if
		else
			{
			dataPtr = (int*) popStack (stack);
			operand2 = *dataPtr;
			dataPtr = (int*) popStack (stack);
			operand1 = *dataPtr;
			value = calc (operand1, token, operand2);
			dataPtr = (int*) malloc (sizeof (int));
			*dataPtr = value;
			pushStack (stack, dataPtr);
			}	// else
		}	// while
	// the final result is in stack. pop it print it.
	dataPtr = (int*) popStack (stack);
	value = *dataPtr;
	printf ("The result is: %d\n", value);

	// now destroy the stack
	destroyStack (stack);
	return 0;
}	// main


/* ==== isOperator ==== 
	validate operator
		pre token is operator to be validated
		post return true if valid, false if not
*/
bool isOperator (char token)
{
// statements
	if (token == '*'
		|| token == '/'
		|| token == '+'
		|| token == '-')
		return true;
	return false;
}	// isOperator

/* ==== calc ==== 
	given two values and operator, determine value of formula.
		pre operand1 and operand2 are values
			oper is the operator
		post return result of calculation
*/
int calc (int operand1, int oper, int operand2)
{
// local declaration
	int result;

// statements
	switch (oper)
		{
			case '+' : result = operand1 + operand2;
				break;
                        case '-' : result = operand1 - operand2;
                                break;
                        case '*' : result = operand1 * operand2;
                                break;
                        case '/' : result = operand1 / operand2;
                                break;
		}	// switch

	return result;
}	// calc
