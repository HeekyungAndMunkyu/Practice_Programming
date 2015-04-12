#include <stdio.h>
#include <time.h>


int main (void)
{
	// local declarations
	time_t start, end, duration;

	// statements
	start = 0900;
	end = 1700;
	duration = end - start;
	printf ("%d - %d = %d", end, start, duration);
}
