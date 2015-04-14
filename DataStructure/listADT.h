//List ADT Type Definitions
typedef struct node 
	{
	void* dataPtr;
	struct node* link;
	} NODE;

typedef struct 
	{
	int count;
	NODE* pos;
	NODE* head;
	NODE* rear;
	int (*compare) (void* argu1, void* argu2);
	} LIST;

// Prototype Declarations
LIST* createList (int (*compare) (void* argu1, void* argu2));
LIST* destroyList (LIST* list);

int addNode (LIST* pList, void* dataInPtr);
bool removeNode (LIST* pList, void* keyPtr, void** dataOutPtr);

bool searchList (LIST* pList, void* pArgu, void** pDataOut);

bool retrieveNode (LIST* pList, void* pArgu, void** dataOutPtr);
bool traverse (LIST* pList, int fromWhere, void** dataOutPtr);

int listCount (LIST* pList);

bool emptyList (LIST* pList);
bool fullList (LIST* pList);

static int _insert (LIST* pList, NODE* pPre, void* dataInPtr);
static void _delete (LIST* pList, NODE* pPre, NODE* pLoc, void** dataOutPtr);
static bool _search (LIST* pList, NODE** pPre, NODE** pLoc, void* pArgu);

/* ========== createList ========== */
/* ==========  ========== */
/* ==========  ========== */
/* ==========  ========== */
/* ==========  ========== */
/* ==========  ========== */
/* ==========  ========== */
/* ==========  ========== */
/* ==========  ========== */
/* ==========  ========== */
/* ========== _insert ========== */
        {
        // local definitions
        NODE* pNew;

        // statements
        if (!(pNew = (NODE*) malloc (sizeof (NODE))))
                return false;

        pNew->dataPtr = dataInPtr;
        pNew->link = NULL;

        if (pPre == NULL)
                {
                // adding before first node or to empty list.
		}	// if
	}	// _insert

/* ==========  ========== */
/* ========== _search ========== */
static bool _search (LIST* pList, NODE** pPre, NODE** pLoc, void* pArgu)
	{
	// Macro Definition
	#define COMPARE ( ((* pList->compare) (pArgu, (*pLoc)->dataPtr)) )
	#define COMPARE_LAST ( (* pList->compare) (pArgu, pList->rear->dataPtr))

	// Local definitions
	int result;

	// statements
	*pPre = NULL;
	*pLoc = pList->head;
	if (pList->count == 0)
		return false;

		//

