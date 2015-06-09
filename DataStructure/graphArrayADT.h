#include <stdbool.h>
#include "stackADT.h"

//Data Structure
typedef struct
  {
  void* dataPtr;
  int processed; //0 = not processed, 1 = pushed to stack, 2 = popped out of stack
  } VERTEX;

typedef struct
  {
  int count;
  int rootLoc;
  int (*compare) (void* argu1, void* argu2);
  void* vertexVector; // later, VERTEX vertexVector [numVertex]
  void* adjacencyMatrix; // later, int adjacencyMatrix [numVertex][numVertex]
  } GRAPH;



//Algorithms
graphCreate
graphDestory

graphAddVertex
graphDelVertex
graphAddArc
graphDelArc

void graphBFTraverse (GRAPH* graph);
void graphDFTraverse (GRAPH* graph);

int graphCount (GRAPH* graph);
bool graphFull (GRAPH* graph);
bool graphEmpty (GRAPH* graph);


/* ========== graphBFTraverse ========== */

/* ========== graphDFTraverse ========== */
void graphDFTraverse (GRAPH* graph)
  {
    //Data structure
    STACK* stack;
    int processed [graphCount (graph)];
    int current;

    //Algorithms
    //while not all popped out of stack (not all 2)
    while (processed != int[graphCount (graph)])
      {
      if emptyStack (stack)
          {
        //newNum = first unprocessed vertex in processed vector
          for (i = 0; i < graph->count; i++)
              {
              if (processed[i] == 0)
                //pushStack (stack, newNum)
                pushStack (stack, i);
              
              }
        
          }
      else
          {
        //current = popStack (stack);
        current = popStack (stack);
        //for all adjacency nodes of 'current' node
        for (i = 0; i< graph->count; i++)
            {
            //if processed != 1 or != 2
            if (graph->adjacencyMatrix[current][i] == 0)
              //pushStack (stack, adjacency node)
              pushStack (stack, i)
            } //for
          }//else
      }// while not all popped out of stack (not all 2)
  }
  
/* ==========  ========== */
/* ==========  ========== */
/* ==========  ========== */
/* ==========  ========== */
/* ==========  ========== */
/* ==========  ========== */
/* ==========  ========== */
/* ==========  ========== */
