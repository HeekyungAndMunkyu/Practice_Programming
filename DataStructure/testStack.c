#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "stackADT_kbs.h"

int main (void)
{
STACK* stack;
int data;
int* pNum;

stack = createStack ();

int i;
for (i = 0; i < 5; i++)
  {
  pNum = (int*) malloc (sizeof (int));
  *pNum = i;
  printf("insert %d\n", *pNum);
  pushStack (stack, pNum);
  //printf("count: %d\n", stackCount (stack));
  //data = *(int*) popStack (stack);
  //printf("%d popped\n", data);
}


while (!emptyStack (stack))
  {

  data = *(int*) popStack (stack);
  printf("%d popped\n", data);
}

/*
char a = 'a';
char b = 'b';
pushStack (stack, &a);
printf("%s pushed\n", &a);
pushStack (stack, &b);
printf("%s pushed\n", &b);


char data;
data = *(char*) popStack (stack);
printf("%s popped\n", &data);
data = *(char*) popStack (stack);
printf("%s popped\n", &data);
printf("%d", emptyStack (stack));
*/

return 0;
}
