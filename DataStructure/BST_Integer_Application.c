/* This program builds and prints a BST */
#include <stdio.h>
#include <stdlib.h>
#include "BinarySearchTreeADT.h"

//Prototype Declarations
int compareInt (void* num1, void* num2);
void printBST (void* num1);

int main (void)
{
// Local Definitions
BST_TREE* BSTRoot;
int* dataPtr;
int dataIn = +1;
int delKey;

// Statements
printf("Begin BST Demonstration\n");

BSTRoot = BST_Create (compareInt);

// Build Tree


do
	{
	printf("\nEnter a list of positive integers:\n");
	printf("\t\tTo stop, enter a negative integer.\n");
	printf("\t\tTo delete a number, enter 0.\n");
	printf("\nEnter a number: ");
	scanf("%d", &dataIn);
	if (dataIn == 0)
		{
			printf("\t\tWhat number do you want to delete? Enter: \n");
			scanf("%d", &delKey);
			BST_Delete (BSTRoot, &delKey);

			printf("\tNow in BST: \n");
			BST_Traverse (BSTRoot, printBST);
		}

	if (dataIn > 0)
		{
		dataPtr = (int*) malloc (sizeof (int));
		if (!dataPtr)
			{
			printf("Memory Overflow in add\n"),
			exit(100);
			}// if overflow
		*dataPtr = dataIn;
		BST_Insert (BSTRoot, dataPtr);

		printf("\tNow in BST: \n");
		BST_Traverse (BSTRoot, printBST);

		}// valid data
	} while (dataIn > -1);

printf("\nBST contains:\n");
BST_Traverse (BSTRoot, printBST);

printf("\nEnd BST Demonstration\n");



//remove later
//printf ("%d\n", BST_Count (BSTRoot));
//printf ("%d\n", BST_Empty (BSTRoot));



return 0;
}// main


/*========== compareInt ========== */
int compareInt (void* num1, void* num2)
	{
	//local definitions
	int key1;
	int key2;

	//statements
	key1 = *(int*)num1;
	key2 = *(int*)num2;
	if (key1 < key2)
		return -1;
	if (key1 == key2)
		return 0;
	return +1;
	}// compareInt


/*========== printBST ========== */
void printBST (void* num1)
	{
	printf("%4d\n", *(int*) num1);
	return;
	} // printBST
