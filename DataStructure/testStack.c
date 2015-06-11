#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "stackADT.h"

int main (void)
{
STACK* stack;
int data;

stack = createStack ();

int i;
for (i = 0; i < 2; i++)
  {
  printf("insert %d\n", i);
  pushStack (stack, &i);
  printf("count: %d\n", stackCount (stack));
  //data = *(int*) popStack (stack);
  //printf("%d popped\n", data);
}


while (!emptyStack (stack))
  {

  data = *(int*) popStack (stack);
  printf("%d popped\n", data);
}


return 0;
}
