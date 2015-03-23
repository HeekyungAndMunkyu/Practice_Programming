#include <stdio.h>

// Prototype Statements
	void towers (int n, char source,
			char dest, char auxiliary);

int main (void)
{
	int numDisks;

	printf ("Please enter number of disks: ");
	scanf ("%d", &numDisks);

	printf("Start Towers of Hanoi. \n\n");

	towers (numDisks, 'A', 'C', 'B');

	printf("\nI Hope you didn't select 64 "
		"and end the world!\n");
	return 0;
}	// main

/* ================= towers ==================
*/
void towers (int n, char source,
		char dest, char auxiliary)
{
	static int step = 0;

	printf("Towers (%d, %c, %c, %c)\n",
			n, source, dest, auxiliary);

	if (n == 1)
		printf("\t\tStep %3d: Move from %c to %c\n",
			++step, source, dest);

	else
		{
		towers (n - 1, source, auxiliary, dest);
		printf("\t\tStep %3d: Move from %c to %c\n",
			++step, source, dest);
		towers (n - 1, auxiliary, dest, source);
		}	// if - else
	return;
}	// towers
