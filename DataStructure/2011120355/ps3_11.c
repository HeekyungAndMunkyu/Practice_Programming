#include <stdio.h>
#include "stackADT.h"

int main (void)
{
//local deifinitions
	STACK* stack;
	int num;
	int* digit;

//statements
	//create stack
	stack = createStack();

	//prompt and read a number
	printf ("Enter any decimal number to convert into hexadecimal number: ");
	scanf ("%d", &num);

	//create hexadecimal numbers(0~15) and push to stack
	while (num > 0)
		{
			digit = (int*) malloc (sizeof(int));
			*digit = num % 16;
			pushStack (stack, digit);
			num /= 16;
		}

	//binary number created. now print it
	printf ("The hexadecimal number is: ");
	while (!emptyStack (stack))
		{
			digit = (int*)popStack(stack);
			if (*digit == 10)
				printf ("A");
                        else if (*digit == 11)
				printf ("B");
                        else if (*digit == 12)
				printf ("C");
                        else if (*digit == 13)
				printf ("D");
                        else if (*digit == 14)
				printf ("E");
                        else if (*digit == 15)
				printf ("F");
			else
				printf ("%d", *digit);
	
		}
	printf ("\n");
	//destorying stack
	destroyStack (stack);
	return 0;
}	//makn
