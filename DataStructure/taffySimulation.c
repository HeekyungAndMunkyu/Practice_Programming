#include <stdio.h>
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
	
// algorithms
void newCustomer (QUEUE* queue, int clock, int custNum);
void serverFree (QUEUE* queue, int clock, STATUS* status, bool moreCusts);
void svcComplete (QUEUE* queue, int clock, STATUS* status, STATS* stats, \
		bool moreCusts);
void printStats (STATS* stats);

// main
int main (void)
	{
	// local declarations
	QUEUE* queue;
	int clock;
	bool moreCusts = false;
	int custNum = 0;

	// statements
	queue = (QUEUE*) malloc (sizeof (QUEUE));
	queue = createQueue ();
	while (clock <= 480 || moreCusts)
		{		
		newCustomer (queue, clock, custNum);
		serverFree (queue, clock, status, moreCusts);
		svcComplete (queue, clock, status, stats, moreCusts);
		
		if (not emptyQueue (queue))
			{		
			moreCusts = true;
			}	// if 
		clock++;
		}	//end while	
	printStats (stats);
	return 0;
	}




/* ========== newCustomer ==========
	This algorithm determines if a new customer has arrived.
*/
void newCustomer (QUEUE* queue, int clock, int custNum)
	{	
	// local declarations
	int custArrived;
	// statements
	custArrived = rand (4);

	if (custArrived == 4)
		{
		custNum++;
		
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
