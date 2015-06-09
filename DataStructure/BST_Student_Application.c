/* This program builds and prints a student list. */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include "BinarySearchTreeADT.h"

// Structures
typedef struct
	{
	int id;
	char name[40];
	float gpa;
	} STUDENT;

// Prototype Declarations
char getOption (void);
void addStu (BST_TREE* list);
void deleteStu (BST_TREE* list);
void findStu (BST_TREE* list);
void printList (BST_TREE* list);
void testUtilities (BST_TREE* list);
int compareStu (void* stu1, void* stu2);
void processStu (void* dataPtr);



int main (void)
{
// Local Definitions
BST_TREE* list;
char option = ' ';

// Statements
printf("Begin Student List\n");
list = BST_Create (compareStu);

while ( (option = getOption ()) != 'Q')
	{	
	switch (option)
		{
		case 'A': addStu (list);
			break;
		case 'D': deleteStu (list);
			break;
		case 'F': findStu (list);
			break;
		case 'P': printList (list);
			break;
		case 'U': testUtilities (list);
			break;
		}// switch
	}// while
list = BST_Destroy (list);

printf ("\nEnd Student List\n");
return 0;

}// main


/* ========== getOption ========== */
char getOption (void)
	{
	// local definitions
	char option;
	bool error;

	// statements
	printf("\n ===== MENU =====\n");
	printf("A Add Student\n");
	printf("D Delete Student\n");
	printf("F Find Students\n");
	printf("P Print Class List\n");
	printf("U Show Utilities\n");
	printf("Q Quit\n");

	do
		{
		printf("\nEnter Option: ");
		scanf("%c", &option);
		option = toupper(option);

		if (option == 'A' || option == 'D'\
		|| option == 'F' || option == 'P'\
		|| option == 'U' || option == 'Q' )
			error = false;
		else
			{
			//remove later
			//printf ("\nThe option typed was:%s.", &option);				// \n has been typed

			printf("Invalid option. Please re-enter: ");
			error = true;
			}// else
		} while (error == true);
	return option;
	}// getOption

/* ========== addStu ========== */
void addStu (BST_TREE* list)
	{
	// Local Definitions
	STUDENT* stuPtr;

	// Statements
	stuPtr = (STUDENT*) malloc (sizeof (STUDENT));
	if (!stuPtr)
		printf("Memory Overflow in add\n"), exit(101);

	printf("Enter student id:   ");
	scanf("%d", &(stuPtr->id));
	printf("Enter student name:   ");
	scanf("%39s", stuPtr->name); // why no &?
	printf("Enter student gpa:   ");
	scanf("%f", &(stuPtr->gpa));
	
	BST_Insert (list, stuPtr);
	}// addStu


/* ========== deleteStu ========== */
void deleteStu (BST_TREE* list)
	{
	//Local Definitions
	int id;
	int* idPtr = &id;

	// Statements
	printf("Enter student id: ");
	scanf("%d", idPtr);

	if (!BST_Delete (list, idPtr))
		printf("ERROR: No Student: %0d\n", *idPtr);
	}// deleteStu


/* ========== findStu ========== */
void findStu (BST_TREE* list)
	{
	// Local definitions
	int id;
	STUDENT* stuPtr;

	// Statements
	printf("Enter student id: ");
	scanf("%d", &id);

	stuPtr = (STUDENT*) BST_Retreive (list, &id);
	if (stuPtr)
		{
		printf("Student id: %04d\n", id);
		printf("Student name: %s\n", stuPtr->name);
		printf("Student gpa: %4.1f\n", stuPtr->gpa);
		}//if
	else
		printf("Student %d not in file\n", id);
	}// findStu


/* ========== printList ========== */
void printList (BST_TREE* list)
	{
	// Statements
	printf("\nStudent List:\n");
	BST_Traverse (list, processStu);
	printf("End of Student List\n");
	return;
	} // printList


/* ========== testUtilities ========== */
void testUtilities (BST_TREE* list)
	{
	printf("Tree contains %3d nodes: \n", BST_Count (list));
	if (BST_Empty (list))
		printf("The tree IS empty\n");
	else
		printf("The tree IS NOT empty\n");
	if (BST_Full (list))
		printf("The tree IS full\a\n");
	else
		printf("The tree IS NOT full\n");
	return;
	}// testUtilities


/* ========== compareStu ========== */
int compareStu (void* stu1, void* stu2)
	{
	//Local Definitions
	STUDENT s1;
	STUDENT s2;

	//Statements
	s1 = *(STUDENT*)stu1;
	s2 = *(STUDENT*)stu2;

	if (s1.id < s2.id)
		return -1;
	if (s1.id == s2.id)
		return 0;
	return +1;
	} // compareStu


/* ========== processStu ========== */
void processStu (void* stuPtr)
	{
	// local definitions
	STUDENT aStu;

	//Statements
	aStu = *(STUDENT*) stuPtr;
	printf ("%04d  %-40s  %4.1f\n", aStu.id, aStu.name, aStu.gpa);
	return;
	}//processStu
