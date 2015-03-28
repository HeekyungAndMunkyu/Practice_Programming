#include <stdio.h>

// Data type
typedef struct node {
  void* dataPtr;
  STACK_NODE* link;
} STACK_NODE;

typedef struct node {
  int count;
  STACK_NODE* top;
} STACK;

// Data operations
STACK createStack () {
  // Local Declarations
  STACK stack;

  //
  stack = (STACK) malloc(size of (STACK))
  stack->count = 0;
  stack->top = NULL;

  return stack;
}
