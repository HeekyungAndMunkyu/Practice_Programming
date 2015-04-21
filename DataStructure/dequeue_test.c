#include "queueADT_dequeue_test.h"
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
dequeue(queue, dataPtr);

printf ("%d", *(int*)dataPtr);

destroyQueue(queue);

return 0;
}
