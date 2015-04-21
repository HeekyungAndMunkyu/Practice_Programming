#include "queueADT.h"
#include <stdio.h>
#include <stdlib.h>

int main (void)
{
QUEUE* queue;
int* a;
*a = 7;
int* dataPtr;


queue = createQueue();
enqueue(queue, a);
dequeue(queue, (void*)&dataPtr);

printf ("%d", *dataPtr);

destroyQueue(queue);

return 0;
}
