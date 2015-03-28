#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Structure Declarations
typedef struct node
  {
  void* dataPtr;
  struct node* link;
  } STACK_NODE;

typedef struct
  {
  int count;
  STACK_NODE* top;
  } STACK;

// Prototype Declarations
STACK* createStack (void);
bool pushStack (STACK* stack, void* dataInPtr);
void* popStack (STACK* stack);
void* stackTop (STACK* stack);
bool emptyStack (STACK* stack);
bool fullStack (STACK* stack);
int stackCount (STACK* stack);
STACK* destroyStack (STACK* stack);


/* =============== createStack ==================
  Creates an empty stack
    Pre Nothing
    Post Returns pointer to a null stack
      -or- NULL if overflow
*/
STACK* createStack (void)
{
  // Local Declarations
  STACK* stack;

  // Statements
  stack = (STACK*) malloc(sizeof (STACK))
  if (stack)
    {
      stack->count = 0;
      stack->top = NULL;
    } // if

  return stack;
} // createStack


/* ================ pushStack =================
    Pre stack: STACK*
        dataInPtr: data* to be inserted

    Post data inserted into stack
    Return true if successful; flase if underflow

*/
bool pushStack (STACK* stack, void* dataInPtr)
{
  // Local Declarations
  STACK_NODE* newPtr;

  // Statements
  newPtr = (STACK_NODE*) malloc(sizeof(STACK_NODE));
  if (!newPtr)
    return false;

  newPtr->dataPtr = dataInPtr;
  newPtr->link = stack->top;
  stack->top = newPtr;

  (stack->count)++;
  return true;
} // pushStack


/* ================ popStack ====================

*/
void* popStack (STACK* stack)
{
  //Local Definitions
  void* dataOutPtr;
  //Statements
  dataOutPtr = stack->top;
  stack->top = stack->top->link;
  stack->top->link = NULL;
  
  return dataOutPtr;
}
