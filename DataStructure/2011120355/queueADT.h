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
bool queueFront (QUEUE* queue, void** itemPtr);
bool queueRear (QUEUE* queue, void** itemPtr);
int queueCount (QUEUE* queue);

bool emptyQueue (QUEUE* queue);
bool fullQueue (QUEUE* queue);


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


/* ============ destoryQueue============= */
QUEUE* destroyQueue (QUEUE* queue)
	{
		//Local Definitions
		QUEUE_NODE* deletePtr;

		// statements
		if (queue)
			{	
				while (queue->front != NULL)
					{
						free (queue->front->dataPtr);
						deletePtr = queue->front;
						queue->front = queue->front->next;
						free (deletePtr);
					}	// while
				free (queue);
			}	// if
		return NULL;
	}	// destoryQueue

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
/* ============ queueFront ============= */
bool queueFront (QUEUE* queue, void** itemPtr)
{	
	// statements
	if (!queue->count)
	{
		return false;
	}	// if
	else
	{
		*itemPtr = queue->front->dataPtr;
		return true;
	}	// else
}	// queueFront
/* ============ queueRear ============= */
bool queueRear (QUEUE* queue, void** itemPtr)
{
        // statements
        if (!queue->count)
        {
                return false;
        }       // if
        else
        {
                *itemPtr = queue->rear->dataPtr;
                return true;
        }       // else
}       // queueFront

/* ============ queueCount ============= */
int queueCount (QUEUE* queue)
{
  return queue->count;

}
/* ============ emptyQueue ============= */
bool emptyQueue (QUEUE* queue)
	{	
		return (queue->count == 0);
	}	// emptyQueue

/* ============ fillQueue ============= */
bool fillQueue (QUEUE* queue)
{
	// local definitions
	QUEUE_NODE* temp;
	// statements
	temp = (QUEUE_NODE*) malloc (sizeof (QUEUE_NODE));
	if (temp)
	{
		free (temp);
		return true;
	}	// if
	return false;
}	// fillQueue
