#include <stdio.h>
#include <stdbool.h>
#include "stackADT.h"
#include <stdlib.h>

int main (void)
{
//Local definitions
	bool done = false;
	int* dataPtr;

	STACK* stack;

//statmentes
	stack = createStack ();

	while (!done)
		{
			dataPtr = (int*) malloc (sizeof(int));
			printf ("Enter a number: <EOF> to stop: ");
			scanf ("%d", dataPtr);
			if (*dataPtr == EOF || fullStack (stack))
				done = true;
			else
				pushStack (stack, dataPtr);
		}	// while
	printf ("\n\nThe list of numbers reversed:\n");
	while (!emptyStack (stack))
		{
			dataPtr = (int*)popStack (stack);
			printf ("%3d\n", *dataPtr);
			free (dataPtr);
		}	// while
	destroyStack (stack);
	return 0;
}	//main
