/*  1. Receive vertex & arc inputs
    2. graphDFTraverse
    3. graphBFTraverse
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
//#include "stackADT.h"
//#include "queueADT.h"

//Data structure
typedef struct {
  void* vector;
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
    scanf("%s", &option);
      //switch
      switch (option)
      {
      //1. receive vertex inputs
      case 'v':
        scanf("%d", &vertex);
        addVertex (graph, &vertex);
        break;

      //2. receive arc inputs
      case 'a':
        printf("  From which number: \n");
        scanf("%d", &fromData);
        printf("  To which number: \n");
        scanf("%d", &toData);
        addArc (graph, &fromData, &toData);
        break;
      //3. graphDFTraverse
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
/* =========== addArc ========== */
/* =========== graphDFTraverse ========== */
/* =========== graphBFTraverse ========== */
