#include <stdio.h>
#include <stdlib.h>

//void graphBFS ();
//void graphDFS ();

int main (void) {
  //Data Structure
  int vertex[4] = {1, 2, 3, 4};
  int processed[4] = {0, 0, 0, 0};
  int adjacencyMatrix[4][4] = {{0, 1, 1, 0}, \
                                {0, 0, 0, 1}, \
                                {0, 0, 0, 1}, \
                                {0, 0, 0, 0}};

  //Algorithms
  char option;

  printf("b: to do BFTraverse\n");
  printf("d: to do DFTraverse\n");
  scanf("%s", &option);

  switch {
    case 'b':


      break;
    case 'd':

      break;
  }


  return 0;
}

/* ==== graphBFS ==== */
//void graphBFS (GRAPH* graph)
{

}


/* === graphDFS === */
//void graphDFS (GRAPH* graph)
{

}
