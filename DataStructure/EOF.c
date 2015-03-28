#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int main (void)
{
	int* dataPtr;
	
	// statements
	dataPtr = (int*) malloc (sizeof(int));
	printf ("Enter");
	scanf("%d", dataPtr);
	if (*dataPtr == -1)
		printf ("EOF");
	return 0;
}
