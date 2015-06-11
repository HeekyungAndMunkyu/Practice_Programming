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

  //Algorithms
  graph = (GRAPH*) createGraph (maxSize);

  //Show options
  //Receive option
    //switch
    //1. receive vertex inputs
    //2. receive arc inputs
    //3. graphDFTraverse
    //4. graphBFTraverse

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
