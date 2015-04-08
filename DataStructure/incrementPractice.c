#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


int main (void)
{
int* num;

num = (int*) malloc (sizeof (int));

*num = 0;


while (*num <= 10)
	{
	printf ("%d", *num);
	(*num)++;
	}
return 0;
}
