#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct node{
	void* dataPtr;
	struct node* link;
}STACK_NODE;

typedef struct {
	int count;
	STACK_NODE* top;
}STACK;


STACK* createStack(void);
bool pushStack(STACK* stack, void* dataInPtr);
void* popStack(STACK* stack);
STACK* destroyStack(STACK* stack);
bool emptyStack(STACK* stack);

bool emptyStack(STACK* stack){
	return (stack->count == 0);
}

STACK* destroyStack(STACK* stack){
	STACK_NODE* temp;

	if (stack){
		while (stack->top != NULL){
			free(stack->top->dataPtr);

			temp = stack->top;
			stack->top = stack->top->link;
			free(temp);
		}
		free(stack);
	}
	return NULL;
}

STACK* createStack(void){
	STACK* stack;

	stack = (STACK*)malloc(sizeof(STACK));
	if (stack){
		stack->count = 0;
		stack->top = NULL;
	}
	return stack;
}

bool pushStack(STACK* stack, void* dataInPtr){
	STACK_NODE* newPtr;

	newPtr = (STACK_NODE*)malloc(sizeof(STACK_NODE));
	if (!newPtr)
		return false;
	
	newPtr->dataPtr = dataInPtr;
	
	newPtr->link = stack->top;
	stack->top = newPtr;

	//printf("Stack input : %d \n", *(int*)(stack->top->dataPtr));

	(stack->count)++;
	return true;
}

void* popStack(STACK* stack){
	void* dataOutPtr = NULL;
	STACK_NODE* temp;

	if (!stack->top){
		return NULL;
	}
	
	if (stack->top){
		temp = stack->top;
		stack->top = stack->top->link;

		dataOutPtr = temp->dataPtr;
		free(temp);
	}

	(stack->count)--;
	return dataOutPtr;
}
