#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "queueADT.h"

// data types
typedef struct
	{
	int custNum;
	int arriveTime;
	int startTime;
	int svcTime;
	} STATUS;

typedef struct
	{
	int numCust;
	int totSvcTime;
	int totWaitTime;
	int maxQueueSize;
	} STATS;

typedef struct
	{
		int custNum;
		int arriveTime;
	}	CUST_DATA;

// algorithms
void newCustomer (QUEUE* queue, int* clockTime, int* custNum);
void serverFree (QUEUE* queue, int* clockTime, STATUS* status, bool* moreCusts);
void svcComplete (QUEUE* queue, int* clockTime, STATUS* status, STATS* stats, \
		bool moreCusts);
void printStats (STATS* stats);

// main
int main (void)
	{
	// local declarations
	QUEUE* queue;
	int* clockTime;
	bool* moreCusts;
	int* custNum;

	// statements
	queue = (QUEUE*) malloc (sizeof (QUEUE));
	clockTime = (int*) malloc (sizeof (int));
	moreCusts = (bool*) malloc (sizeof (bool));
	custNum = (int*) malloc (sizeof (int));

	queue = createQueue ();
	*clockTime = 0;
	*custNum = 0;

	while (*clockTime <= 10 || moreCusts)
		{
		newCustomer (queue, clockTime, custNum);
		int countcount;
		countcount = queueCount (queue);
		printf ("clockTime:%d, custNum: %d, queueCount:%d", *clockTime, *custNum, countcount);
		}
		/* serverFree (queue, clockTime, status, moreCusts);
		svcComplete (queue, clockTime, status, stats, moreCusts);

		if (not emptyQueue (queue))
			{
			moreCusts = true;
			}	// if
		clockTime++;
		}	//end while
	printStats (stats);
	*/
	return 0;
	}




/* ========== newCustomer ==========
	This algorithm determines if a new customer has arrived.
*/
void newCustomer (QUEUE* queue, int* clockTime, int* custNum)
	{
	// local declarations
	int custArrived;
	CUST_DATA* custData;

	// statements
	custArrived = rand () % 4;
	if (custArrived == 0)
		{
		(*custNum)++;
		custData = (CUST_DATA*) malloc (sizeof (CUST_DATA));
		custData->custNum = *custNum;
		custData->arriveTime = *clockTime;
		enqueue (queue, custData);
		}	// if
	}	// newCustomer

/* ========== serverFree ==========
	This algorithm determines if the server is idle and if so starts serving a new customer.
*/


/* ========== svcComplete ==========
	Determines if the current customer's processing is complete.

*/

/* ========== printStats ==========
	Prints the statistics for the simulation.
*/
