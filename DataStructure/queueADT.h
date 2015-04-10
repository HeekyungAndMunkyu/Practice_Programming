#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


// data type
typedef struct node
  {
    void* dataPtr;
    struct node* next;
  } QUEUE_NODE;

typedef struct
  {
    QUEUE_NODE* front;
    QUEUE_NODE* rear;
    int count;
  } QUEUE;

// prototype declarations
QUEUE* createQueue (void);
QUEUE* destroyQueue (QUEUE* queue);

bool dequeue (QUEUE* queue, void** itemPtr);
bool enqueue (QUEUE* queue, void* itmePtr);
int queueCount (QUEUE* queue);

bool emptyQueue (QUEUE* queue);



/* ============ createQueue ============= */
QUEUE* createQueue (void)
{
  // local definitions
  QUEUE* queue;

  // statements
  queue = (QUEUE*) malloc (sizeof (QUEUE));
  if (queue)
    {
      queue->front = NULL;
      queue->rear = NULL;
      queue->count = 0;
    }

  return queue;
}


/* ============ createQueue ============= */
/* ============ dequeue ============= */
bool dequeue (QUEUE* queue, void** itemPtr)
	{
	// local definitions
	QUEUE_NODE* deleteLoc;

	// statements
	if (!queue->count)
		return false;

	*itemPtr = queue->front->dataPtr;
	deleteLoc = queue->front;

	if (queue->count == 1)
		queue->rear = queue->front = NULL;
	else
		queue->front = queue->front->next;

	(queue->count)--;
	free(deleteLoc);

	return true;
	}	// dequeue

/* ============ enqueue ============= */
bool enqueue (QUEUE* queue, void* itemPtr)
{
  // local definitions
  QUEUE_NODE* newPtr;

  // statements
  if (!(newPtr = (QUEUE_NODE*) malloc (sizeof (QUEUE_NODE))))
    return false;

  newPtr->dataPtr = itemPtr;
  newPtr->next = NULL;

  if (queue->count == 0)
    queue->front = newPtr;
  else
    queue->rear->next = newPtr;

  (queue->count)++;

  queue->rear = newPtr;

  return true;
}
/* ============ createQueue ============= */
int queueCount (QUEUE* queue)
{
  return queue->count;

}
/* ============ createQueue ============= */
bool emptyQueue (QUEUE* queue)
	{	
		return (queue->count == 0);
	}	// emptyQueue
