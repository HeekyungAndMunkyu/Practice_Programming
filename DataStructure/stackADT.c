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
  STACK_NODE* temp;

  //Statements
  if (stack->count == 0)
    dataOutPtr = NULL;
  else
    {
      temp = stack->top;
      dataOutPtr = stack->top->dataPtr;
      stack->top = stack->top->link;
      free(temp);
      (stack->count)--;
    }
  return dataOutPtr;
}



/* ================ stackTop =========================

*/
void* stackTop (STACK* stack)
{
  //Local Definitions
  //Statements
  if (stack->count == 0)
    return NULL;
  else
    return stack->top->dataPtr;
} // stackTop

/* ================== emptyStack =====================
  returns: 1 if the stack is empty; 0 otherwise
*/
bool emptyStack (STACK* stack)
{
  // Statements
  return (stack->count == 0);
} // emptyStack


/* ================= fullStack =======================
  determines if a stack is full
  Full == heap full

  returns: true if heap full; false otherwise
*/
bool fullStack (STACK* stack)
{
  // local definitions
  STACK_NODE* temp;
  // statements
  if ((temp =
    (STACK_NODE*) malloc(sizeof(*(stack->top)))))
    {
      free(temp);
      return false;
    } //if
  // malloc failed
  return true;
} // fullStack




/* ============== stackCount ====================
  returns: int, stack count
*/
int stackCount (STACK* stack)
{
  return stack->count;
}


/* ============== destroyStack ===================
    release all nodes to the heap
  returns: null pointer
*/
STACK* destroyStack (STACK* stack)
{
  //local definitions
  STACK_NODE* temp;
  //statements
  if (stack)
    {
      //Delete all nodes in stack
      while (stack->top != NULL)
        {
          free(stack->top->dataPtr);

          temp = stack->top;
          stack->top = stack->top->link;
          free(temp);
        } // while
      // Stack now empty. Destroy stack head node.
      free(stack);
    }
  return NULL;
} // destoryStack


int main (void)
{
  // local definitions
  STACK* stack;
  // statements
  stack = createStack ();

  int* dataInPtr1 = 1;
  int* dataInPtr2 = 2;

  pushStack (STACK* stack, int* dataInPtr1);
  pushStack (STACK* stack, int* dataInPtr2);
  stackTopDataPtr = stackTop(STACK* stack);
  printf ("%d", *stackTopDataPtr)

}
