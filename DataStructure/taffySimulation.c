#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "queueADT.h"
#include <time.h>

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
void svcComplete (QUEUE* queue, int* clockTime, STATUS* status, STATS* stats, bool* moreCusts);
void printStats (STATS* stats);

// main
int main (void)
	{
	// local declarations
	QUEUE* queue;
	int* clockTime;
	bool* moreCusts;
	int* custNum;
	STATUS* status;
	STATS* stats;
	
	// statements
	queue = (QUEUE*) malloc (sizeof (QUEUE));
	clockTime = (int*) malloc (sizeof (int));
	moreCusts = (bool*) malloc (sizeof (bool));
	custNum = (int*) malloc (sizeof (int));
	status = (STATUS*) malloc (sizeof (STATUS));
	stats = (STATS*) malloc (sizeof (STATS));
	
	queue = createQueue ();
	*clockTime = 0;
	*custNum = 0;
	// status variables?
	// stats variables?

	while (*clockTime <= 480 || *moreCusts)
		{
		newCustomer (queue, clockTime, custNum);
		serverFree (queue, clockTime, status, moreCusts);
		svcComplete (queue, clockTime, status, stats, moreCusts);

		if (!emptyQueue (queue))
			{
			*moreCusts = true;
			}	// if
		(*clockTime)++;
		}	//end while
	printStats (stats);
	
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
	if (*clockTime > 480)
		return;
	custArrived = rand () % 4;
	if (custArrived == 3)

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
void serverFree (QUEUE* queue, int* clockTime, STATUS* status, bool* moreCusts)
	{
	// local definitions
	CUST_DATA* custData;

	// statements
	custData = (CUST_DATA*) malloc (sizeof (CUST_DATA));

	if (*clockTime > status->startTime + status->svcTime - 1)
		{
		if (!emptyQueue (queue))
			{
			if (dequeue (queue, (void*)&custData))
				{
				status->custNum = custData->custNum;
				status->arriveTime = custData->arriveTime;
				status->startTime = *clockTime;
				status->svcTime = (rand () % 10) + 1;
			
				*moreCusts = true;		
				}	// if
			}	// if
		}	// if
	}	// serverFree


/* ========== svcComplete ==========
	Determines if the current customer's processing is complete.

*/
void svcComplete (QUEUE* queue, int* clockTime, STATUS* status, STATS* stats, bool* moreCusts)
	{
	// local definitions
	int waitTime;
	int queueSize;

	// statements
	if (*clockTime == status->startTime + status->svcTime -1)
		{	
		waitTime = status->startTime - status->arriveTime;
		(stats->numCust)++;
		stats->totSvcTime += status->svcTime;
		stats->totWaitTime += waitTime;
		queueSize = queueCount (queue);
		
		if (stats->maxQueueSize < queueSize)
			{	
			stats->maxQueueSize = queueSize;	
			}	// if
		printf ("Customer number: %d\n\
Customer arrive time: %d:%d\n\
Customer start time: %d:%d\n\
Customer service time: %d minutes\n\
Customer wait time: %d minutes\n\
Current queue size: %d\n\n",\
			status->custNum, ((status->arriveTime) / 60) + 9, (status->arriveTime) % 60,\
			((status->startTime) / 60) + 9, (status->startTime) % 60, status->svcTime,\
			waitTime, queueSize);
		*moreCusts = false; //why?
		}	//if
	}	// svcComplete

/* ========== printStats ==========
	Prints the statistics for the simulation.
*/
void printStats (STATS* stats)
	{
	// local definitions
	float avgSvcTime;
	float avgWaitTime;

	// statements
	printf ("Simulation Statistics:\n");
	printf ("Total customers: %d\n", stats->numCust);
	printf ("Total service time: %d hours %d\n", \
		(stats->totSvcTime)/ 60, (stats->totSvcTime) % 60);
	avgSvcTime = (float) stats->totSvcTime / stats->numCust;
	printf ("Average service time: %d minutes\n", avgSvcTime);
	avgWaitTime = (float) stats->totWaitTime / stats->numCust;
	printf ("Average wait time: %d minutes\n", avgWaitTime);
	printf ("Maximum queue size: %d\n", stats->maxQueueSize);	
	}	// printStats
