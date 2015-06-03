#include <stdbool.h>

typedef struct {
	void** heapAry;
	int last;
	int size;
	int (*compare) (void* argu1, void* argu2);
	int maxSize;
} HEAP;

//Prototype Declarations
HEAP* heapCreate (int maxSize, int (*compare) (void* argu1, void* argu2));

bool heapInsert (HEAP* heap, void* dataPtr);
bool heapDelete (HEAP* heap, void* dataOutPtr);

int heapCount (HEAP* heap);

bool heapFull (HEAP* heap);
bool heapEmpty (HEAP* heap);

void heapDestroy (HEAP* heap);

static void _reheapUp (HEAP* heap, int childLoc);
static void _reheapDown (HEAP* heap, int root);


/* ========== heapCreate ========== */
#include <math.h>

HEAP* heapCreate (int maxSize, int (*compare) (void* argu1, void* argu2))
{
//Local Definitions
HEAP* heap;

//Statements
heap = (HEAP*) malloc (sizeof (HEAP));
if (!heap)
	return NULL;

heap->last = -1;
heap->compare = compare;

//Force heap size to power of 2 -1
heap->maxSize = (int) pow (2, ceil(log2(maxSize))) - 1;
heap->heapAry = (void*) calloc(heap->maxSize, sizeof(void*));

return heap;
}


/* ========== heapInsert  ========== */
bool heapInsert (HEAP* heap, void* dataPtr)
{
//Data Structure

//Algorithms
	if (heap->size == 0)	//heap empty
		{
		heap->size = 1;
		heap->last = 0;
		heap->heapAry[heap->last] = dataPtr;
		return true;
		}	// if

	if (heap->last == heap->maxSize - 1)	//heap full
		return false;

	// Neither empty nor full
	++(heap->last)
	++(heap->size);
	heap->heapAry[heap->last] = dataPtr;
	_reheapUp(heap, heap->last);

	return true;
}


/* ========== _reheapUp ========== */
static void _reheapUp (HEAP* heap, int childLoc)
{
//Data Structure
	int parent;
	void** heapAry;
	void* hold;

//Algorithms
	//if not at root of heap -- index 0
	if (childLoc)
		{
		heapAry = heap->heapAry;
		parent = (childLoc - 1) / 2;
		
		if (heap->compare (heapAry[childLoc], heapAry[parent]) > 0)
			// child > parent -- swap
			{
			hold = heapAry[parent];
			heapAry[parent] = heapAry[childLoc];
			heapAry[childLoc] = hold;
			_reheapUp(heap, parent);
			}	// if heap[]
		}	// if newNode
	return;
}


/* ========== heapDelete ========== */
bool heapDelete (HEAP* heap, void* dataOutPtr)
{
//Data Structure

//Algorithms
if (heap->size == 0)
	return false;
*dataOutPtr = heap->heapAry[0];
heap->heapAry[0] = heap->heapAry[heap->last];
(heap->size)--;
(heap->last)--;
_reheapDown (heap, 0);
return true;
}
	

/* ========== _reheapDown ========== */
static void _reheapDown (HEAP* heap, int root)
{
//Data Structure
	void* hold;
	void* leftData;
	void* rightData;
	int largeLoc;
	int last;

//Algorithms
	last = heap->last;
	
	// if left subtree exists
	if (root * 2 + 1 >= last)
		{
		leftData = heap->heapAry[root * 2 + 1];
		// if right subtree exists
		if (root * 2 + 2 >= last)	
		        rightData = heap->heapAry[root * 2 + 2];
		else
			rightData = NULL;
		
		// decide largeLoc
		// If no right data or left data is greater
		if ((!rightData) || heap->compare (leftData, rightData) > 0)
			largeLoc = root * 2 + 1;
		else
			largeLoc = root * 2 + 2;

		// If root < larger child
		if (heap->compare (heap->heapAry[root], heap->heapAry[largeLoc]) < 0)
			{
			hold = heap->heapAry[root];
			heap->heapAry[root] = heap->heapAry[largeLoc];
			heap->heapAry[largeLoc] = hold;
			_reheapDown (heap, largeLoc);
			} // if root < larger child
		}	// if left subtree exists
	return;
}


/* ========== heapCount ========== */
int heapCount (HEAP* heap)
{
//Data Structure
//Algorithms
return heap->size;
}


/* ========== heapFull ========== */
bool heapFull (HEAP* heap)
	{
	// DataStructure
	// Algorithms
	return heap->size >= heap->maxSize;
	}

/* ========== heapEmpty ========== */
bool heapEmpty (HEAP* heap)
	{
	return heap->size == 0;
	}


/* ========== heapDestroy ========== */
void heapDestroy (HEAP* heap)
	{
	free(heap->heapAry);
	free(heap);
	return;
	}

/* ==========  ========== */
/* ==========  ========== */
