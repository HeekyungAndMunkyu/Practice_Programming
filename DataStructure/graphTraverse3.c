/*  1. Receive vertex & arc inputs
    2. graphDFTraverse
    3. graphBFTraverse
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "stackADT.h"
#include "queueADT.h"

//Data structure
typedef struct {
  int* vector;
  int** adjMatrix;
  int size;
  int maxSize;
} GRAPH;

//Algorithms
GRAPH* createGraph (int maxSize);
void addVertex (GRAPH* graph, void* dataPtr);
void addArc (GRAPH* graph, void* fromDataPtr, void* toDataPtr);
void graphDFTraverse (GRAPH* graph);
void graphBFTraverse (GRAPH* graph);
int searchLoc (GRAPH* graph, void* dataPtr);

int main (void)
{
  //Data structure
  GRAPH* graph;
  int maxSize = 4;
  char option;
  int vertex;
  int fromData;
  int toData;

  //Algorithms
  graph = (GRAPH*) createGraph (maxSize);

  do
    {
    //Show options
    //Receive option
    printf("\nv : to receive vertex input\n");
    printf("a : to receive arc input\n");
    printf("d : to DFTraverse graph\n");
    printf("b : to BFTraverse graph\n");
    printf("q : to quit\n");
    printf("Please enter an option >>  ");
    scanf("%s", &option);
      //switch
      switch (option)
      {
      //1. receive vertex inputs
      case 'v':
        printf("\n  What number to vertex?:");
        scanf("%d", &vertex);
        addVertex (graph, &vertex);

        //test
        int h;
        for (h = 0; h <graph->size; h++)
          printf("\nat %d, %d", h, graph->vector[h]);

        break;

      //2. receive arc inputs
      case 'a':
        printf("\n  From which number: \n");
        scanf("%d", &fromData);
        printf("  To which number: \n");
        scanf("%d", &toData);
        addArc (graph, &fromData, &toData);
        break;
      //3. graphDFTraverse
      case 'd':
        printf("\nDepth-first Traverse:\n");
        graphDFTraverse (graph);
        break;
      //4. graphBFTraverse
      }//switch
    } while (option != 'q');
  return 0;
}

/* =========== createGraph ========== */
GRAPH* createGraph (int maxSize)
{
  //Data Structure
  GRAPH* graph;

  //Algorithms
  graph = (GRAPH*) malloc (sizeof (GRAPH));
  if (!graph)
    return NULL;

  int* vector = (int*)malloc(sizeof(int)*maxSize);
  graph->vector = vector;

  graph->adjMatrix = (int**)malloc(sizeof(int*)*maxSize);

  int i;
  for (i = 0; i < maxSize; i++)
    {
    // Allocate n number of columns in the matrix
    graph->adjMatrix[i] = (int*)malloc(sizeof(int)*maxSize);
    // For each element, assign the initial value
    int j;
    for (j = 0; j < maxSize; j++) graph->adjMatrix[i][j] = 0;
    }

  graph->size = 0;
  graph->maxSize = maxSize;


  return graph;
}

/* =========== addVertex ========== */
void addVertex (GRAPH* graph, void* dataPtr)
{
  //Data structure
  int num;

  //Algorithms
  num = *(int*)dataPtr;

  graph->vector[graph->size] = num;
  graph->size++;

  return;
}

/* =========== addArc ========== */
void addArc (GRAPH* graph, void* fromDataPtr, void* toDataPtr)
{
  //Data Structue
  int from;
  int to;

  //Algorithms
  from = *(int*)fromDataPtr;
  to = *(int*)toDataPtr;
  //printf("from %d, to %d\n", from, to);
  //printf("[%d][%d]\n", searchLoc(graph, &from),searchLoc(graph, &to));
  //printf("\n\n\n");
  graph->adjMatrix[searchLoc(graph, &from)][searchLoc(graph, &to)] = 1;
  return;
}

/* =========== graphDFTraverse ========== */
void graphDFTraverse (GRAPH* graph)
{
  //Data Structure
  STACK* stack;
  int processed [graph->size];
  int countDown = graph->size;
  int loc1;
  int loc2;

  //Algorithms
  stack = createStack ();
  int i;
  for (i = 0; i < graph->size; i++)
    {
      processed [i] = 0;
    }

  //insert first vertex into stack
  //int first = 0;
  //pushStack (stack, &first);
  //processed[first] = 1;

  //while not every vertex processed or in stack
  while (countDown != 0)
    {
      printf("stack Count: %d\n", stackCount (stack));
      //popStack problem
      //if empty stack
      if (emptyStack (stack))
        {
        //serach 0 processed vector in processed
        for (i = 0; i < graph->size; i++)
          {
            printf("here %d\n", i);
            if (processed [i] == 0)
              loc1 = i;
              break;
          }
        //pushStack
        pushStack (stack, &loc1);
        processed [loc1] = 1;
        printf("%d pushed\n", loc1);
        }//emptyStack
      //else (not empty)
      else
        {
        //popstack
        loc2 = *(int*) popStack (stack);
        countDown--;
        //process vertex
        printf("at %d, %d\n", loc2, graph->vector[loc2]);
        processed [loc2] = 2;
        //insert adjacency vertex if not in stack or not processed
        //for adjacency vertex
        int j;
        for (j = 0; j < graph->size; j++)
          {
            if (graph->adjMatrix[loc2][j] == 1)
              {
                printf("found adjacency node\n");
                //if not in stack or not processed
                if (processed[j] == 0)
                  {
                  pushStack(stack, &j);
                  printf("%d has been pushed\n", j);

                  processed [j] = 1;
                  }
              }
          }//for
        }//else
    }
  return;
}

/* =========== graphBFTraverse ========== */
void graphBFTraverse (GRAPH* graph)
  {
    //Data Structure
    QUEUE* queue;
    int processed [graph->size];
    int countDown = graph->size;
    int loc1;
    int* loc2Ptr;

    //Algorithms
    queue = createQueue ();
    int i;
    for (i = 0; i < graph->size; i++)
      {
        processed [i] = 0;
      }

    //while not every vertex processed or in stack
    while (countDown != 0)
      {
        //if empty queue
        if (emptyQueue (queue))
          {
          //serach 0 processed vector in processed
          for (i = 0; i < graph->size; i++)
            {
              printf("here %d\n", i);
              if (processed [i] == 0)
                loc1 = i;
                break;
            }
          //enqueue
          enqueue (queue, &loc1);
          processed [loc1] = 1;
          }//emptyqueue
        //else (not empty)
        else
          {
          //popstack
          dequeue (queue, (void*)&loc2Ptr);
          countDown--;
          //process vertex
          processed [*loc2Ptr] = 2;
          //insert adjacency vertex if not in stack or not processed
          //for adjacency vertex
          int j;
          for (j = 0; j < graph->size; j++)
            {
              if (graph->adjMatrix[*loc2Ptr][j] == 1)
                {
                  //if not in stack or not processed
                  if (processed[j] == 0)
                    {
                    enqueue(queue, &j);
                    processed [j] = 1;
                    }
                }
            }//for
          }//else
      }
    return;
  }

/* =========== searchLoc ========== */
int searchLoc (GRAPH* graph, void* dataPtr)
{
  //Data structure
  int loc;
  int data;

  //Algorithms
  data = *(int*) dataPtr;
  int i;
  for (i = 0; i < graph->size; i++)
    {
      printf("\nin serachLoc, for %d\n", i);
      if (graph->vector[i] == data)
        {
        loc = i;
        break;
        }//if
    }//for

  return loc;
}
