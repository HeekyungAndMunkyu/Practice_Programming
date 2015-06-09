/* Implement priority queue using heap. */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>

#include "heapADT.h"

// Constant Definitions
const int maxQueue = 20;

// Data Structure
typedef struct {
	int id;
	int priority;
	int serial;
	} CUST;

// Algorithms
int compareCust (void* cust1, void* cust2);
void processPQ (HEAP* heap);
char menu (void);
CUST* getCust (void);

int main (void)
{
	//Data Structure
	HEAP* prQueue;

	//Algorithms
	printf("Begin Priority Queue Demonstration\n");

	prQueue = heapCreate (maxQueue, compareCust);
	processPQ (prQueue);

	printf("End Priority Queue Demonstration\n");

	return 0;
}	// main


/* ========== compareCust =========
	Compare priority based on serial
		Pre Given two CUST
		Post if cust1 > cust2 return +1
			if == return 0
			if <  return -1
*/
int compareCust (void* cust1, void* cust2)
	{
	//Data Structure
	CUST c1;
	CUST c2;

	//Algorithms
	c1 = *(CUST*) cust1;
	c2 = *(CUST*) cust2;

	if (c1.serial < c2.serial)
		return -1;
	else if (c1.serial == c2.serial)
		return 0;
	return +1;
	}


/* ========== processPQ ========= */
void processPQ (HEAP* prQueue)
	{
	//Data Structure
	CUST* cust;
	bool result;
	char option;
	int numCusts = 0;

	//Algorithms
	do
		{
		option = menu ();
		printf("got option!\n");
		switch (option)
			{
			//enter
			case 'e':
			cust = getCust ();
			numCusts++;
			cust->serial = cust->priority * 1000 + (1000 - numCusts);

			result = heapInsert (prQueue, cust);

			//

			printf("size: %d\n", prQueue->size);
			//

			if (!result)
				printf("Error inserting into heap\n"), exit (101);
			break;


			//delete
			case 'd':
			printf("d\n");
			result = heapDelete (prQueue, (void**)&cust);

			//
			printf("size: %d\n", prQueue->size);
			//

			if (!result)
				printf("Error: customer not found\n");
			else
				{
				printf("Customer %4d deleted\n", cust->id);
				numCusts--;
				}	//else
			}	//switch
		} while (option != 'q');
	return;
	}


/* ========== menu ========= */
char menu (void)
	{
	//Data Structure
	char option;
	bool valid;

	//Algorithms
	printf("\n=========== Menu ==========\n");
	printf(" e : Enter Customer Flight\n");
	printf(" d : Delete Customer Flisht\n");
	printf(" q : Quit.\n");
	printf("==========================\n");
	printf("Please enter your choice:  ");

	do
		{
		scanf("%c", &option);
		option = tolower (option);

		switch (option)
			{
			case 'e':
			case 'd':
			case 'q': valid = true;
					break;

			default: printf("Invalid choice. Re-Enter:  ");
					valid = false;
					break;
			}	//switch
		} while (!valid);
	return option;
	}


/* ========== getCust ========= */
CUST* getCust (void)
	{
	//Data Structure
	CUST* cust;

	//Algorithms
	cust = (CUST*) malloc (sizeof (CUST));
	if (!cust)
		printf("Memory overflow in getCust\n"), exit (200);

	printf("Enter customer id:  ");
	scanf("%d", &cust->id);
	printf("Enter customer priority:  ");
	scanf("%d", &cust->priority);

	return cust;
	}
