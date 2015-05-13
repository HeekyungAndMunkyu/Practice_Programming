# -*- coding:utf-8 -*-

class binaryTree(object):
	def __init__(self, value):
		self.value = value
		self.leftBranch = None
		self.rightBranch = None
		self.parent = None
	def setLeftBranch(self, node):
		self.leftBranch = node
	def setRightBranch(self, node):
		self.rightBranch = node
	def setParent(self, node):
		self.parent = node
	def getValue(self):
		return self.value
	def getLeftBranch(self):
		return self.leftBranch
	def getRightBranch(self):
		return self.rightBranch
	def getParent(self):
		return self.parent
	def __str__(self):
		return str(self.value)


n5 = binaryTree(5)
n2 = binaryTree(2)
n1 = binaryTree(1)
n4 = binaryTree(4)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)
n3 = binaryTree(3)

n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
n4.setLeftBranch(n3)
n3.setParent(n4)


# functions
def find6(node):
    return node.getValue() == 6

def find10(node):
    return node.getValue() == 10

def find2(node):
    return node.getValue() == 2


def lt6(node):
    return node.getValue() > 6







def DFSBinary(root, fcn):
	'''
	root: binaryTree
	fcn: function

	return: True if there exists a node that satisfies fcn;
		False otherwise
	'''
	stack = [root]
	while len(stack) > 0:
		if fcn(stack[0]):
			return True
		else:
			temp = stack.pop(0)
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
			if temp.getLeftBranch():
				stack.insert(0, temp.getLeftBranch())
	return False



def BFSBinary(root, fcn):
        '''
        root: binaryTree
        fcn: function

        return: True if there exists a node that satisfies fcn;
                False otherwise
        '''
	queue = [root]
	while len(queue) > 0:
		if fcn(queue[0]):
			return True
		else:
			temp = queue.pop(0)
			if temp.getLeftBranch():
				queue.append(temp.getLeftBranch())
			if temp.getRightBranch():
				queue.append(temp.getRightBranch())
	return False

def DFSBinaryPath(root, fcn):
        '''
        root: binaryTree
        fcn: function

	return: list, of node values
        '''
        stack = [root]
        while len(stack) > 0:
                if fcn(stack[0]):
                        return [e.getValue() for e in TracePath(stack[0])]
                else:
                        temp = stack.pop(0)
                        if temp.getRightBranch():
                                stack.insert(0, temp.getRightBranch())
                        if temp.getLeftBranch():
                                stack.insert(0, temp.getLeftBranch())
        return False

def TracePath(node):
	if not node.getParent():    # no parent
		return [node]
	else:    # parent
		return [node] + TracePath(node.getParent())




def DFSBinaryOrdered(root, fcn, ltFcn):
        '''
        root: binaryTree
        fcn: function

        return: True if there exists a node that satisfies fcn;
                False otherwise
        '''
        stack = [root]
        while len(stack) > 0:
                if fcn(stack[0]):
                        return True
                elif ltFcn(stack[0]):   # stack[0] > 6
                        temp = stack.pop(0)
                        if temp.getLeftBranch():
                                stack.insert(0, temp.getLeftBranch())
                        if temp.getRightBranch():
                                stack.insert(0, temp.getRightBranch())
        return False




# knapsack problem
def buildDTree(sofar, todo):
	'''
	sofar: list (value of a node)
	todo: list, of lists e.g. [[value0, weight0], [value1, weight1]]

	return: binaryTree (decision tree made up of todo values, with and without) 
	'''
	if len(todo) == 0:
		return binaryTree(sofar)
	else:
		withElt = buildDTree(sofar + [todo[0]], todo[1:])
		withoutElt = buildDTree(sofar, todo[1:])
		here = binaryTree(sofar)
		here.setLeftBranch(withElt)
		here.setRightBranch(withoutElt)
		return here
		

# functions

a = [6,3]
b = [7,2]
c = [8,4]
d = [9,5]

treeTest = buildDTree([], [a,b,c,d])

def sumValues(lst):
    vals = [e[0] for e in lst]
    return sum(vals)

def sumWeights(lst):
    wts = [e[1] for e in lst]
    return sum(wts)

def WeightsBelow10(lst):
    return sumWeights(lst) <= 10

def WeightsBelow6(lst):
    return sumWeights(lst) <= 6






def DFSDTree(root, valueFcn, constraintFcn):
	'''
	root: binaryTree (decision tree, where a list is stored)
	valueFcn: function, summing up values (e.g. sumValues)
	constraintFcn: function, constraining sum of weights (e.g. WeightsBelow10)

	return: binaryTree, with the maximum sum of values, of which sum of weights
		less than or equal to constraining int
	'''
	stack = [root]   # [binaryTree (decision tree)]
	best = None
	visited = 0

	while len(stack) > 0:
		visited += 1
		print
		print 'visited', visited
		print 'stack[0] = ', stack[0]
		if constraintFcn(stack[0].getValue()):
			print '    sumWeights <= 10'
			if best == None:
				print '        if best == None'
				best = stack[0]
			elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
				print '        elif stack[0] > best'
				best = stack[0]
			print '    best', best
			temp = stack.pop(0)
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
			if temp.getLeftBranch():
				stack.insert(0, temp.getLeftBranch())
		else:
			stack.pop(0)
	print 'visited', visited
	return best


def BFSDTree(root, valueFcn, constraintFcn):
	'''
        root: binaryTree (decision tree, where a list is stored)
        valueFcn: function, summing up values (e.g. sumValues)
        constraintFcn: function, constraining sum of weights (e.g. WeightsBelow10)

        return: binaryTree, with the maximum sum of values, of which sum of weights
                less than or equal to constraining int
        '''
	queue = [root]
	best = None
	visited = 0
	while len(queue) > 0:
		visited += 1
		if constraintFcn(queue[0].getValue()):
			if best == None:
				best = queue[0]
			elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
				best = queue[0]
			temp = queue.pop(0)
			if temp.getLeftBranch():
				queue.append(temp.getLeftBranch())
			if temp.getRightBranch():
				queue.append(temp.getRightBranch())
		else:
			queue.pop(0)
	print 'visited', visited
	return best




# stop function
def atLeast15(lst):
    return sumValues(lst) >= 15

def DFSDTreeGoodEnough(root, valueFcn, constraintFcn, stop):
        '''
        root: binaryTree (decision tree, where a list is stored)
        valueFcn: function, summing up values (e.g. sumValues)
        constraintFcn: function, constraining sum of weights (e.g. WeightsBelow10)
	stop: function, deciding if sum of values is greater than or equal to 
		a certain number (e.g. atLeast15)

        return: binaryTree, with the sum of values satisfying stop function,
		 of which sum of weights less than or equal to constraining int
	'''
	stack = [root]
	best = None
	visited = 0
	while len(stack) > 0:
		visited += 1
		if constraintFcn(stack[0].getValue()):
			if best == None:
				best = stack[0]
			elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
				best = stack[0]
			if stop(best.getValue()):
				print 'visited', visited
				return best
			temp = stack.pop(0)
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
			if temp.getLeftBranch():
				stack.insert(0, temp.getLeftBranch())
		else:
			stack.pop(0)
	print 'visited', visited
	return best



def BFSDTreeGoodEnough(root, valueFcn, constraintFcn, stop):
        '''
        root: binaryTree (decision tree, where a list is stored)
        valueFcn: function, summing up values (e.g. sumValues)
        constraintFcn: function, constraining sum of weights (e.g. WeightsBelow10)
        stop: function, deciding if sum of values is greater than or equal to 
                a certain number (e.g. atLeast15)

        return: binaryTree, with the sum of values satisfying stop function,
                 of which sum of weights less than or equal to constraining int
        '''
	queue = [root]
        best = None
        visited = 0
        while len(queue) > 0:
            visited += 1
            if constraintFcn(queue[0].getValue()):
                if best == None:
                    best = queue[0]
                    print best.getValue()
                elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
                    best = queue[0]
                    print best.getValue()
                if stopFcn(best.getValue()):
                    print 'visited', visited
                    return best
                temp = queue.pop(0)
                if temp.getLeftBranch():
                    queue.append(temp.getLeftBranch())
                if temp.getRightBranch():
                    queue.append(temp.getRightBranch())
            else:
                queue.pop(0)
        print 'visited', visited
        return best


visited = 0
def DTImplicit(toConsider, avail):
	'''
	toConsider: list, of lists, which are elements of a decision tree
		(e.g. [[1,10],[3,13]])
	avail: int, maximum sum of weights
		
		returns a node value that maximizes the sum of values
		while keeping the sum of weights less than or equal to avail

	return: tuple, of value of solution and solution, where solution is 
		a node value in a decision tree whose sum of values are maximized
		when sum of weights is less than or equal to 'avail'
		(e.g. (5,([1,10],[4,15]) when avail == 25)
	'''
	global visited
	visited += 1
	print
	print '---> inside DTImplicit ', visited
	if toConsider == [] or avail == 0:
		print 'toConsider == [] or avail == 0'
		print
		result = (0, ())
	elif toConsider[0][1] > avail:
		print '    toConsider[0],[1]', toConsider[0][1], '>', 'avail', avail
		print
		result = DTImplicit(toConsider[1:], avail)
	else:
		nextItem = toConsider[0]
		print 'nextItem: ', nextItem
		withVal, withToTake = DTImplicit(toConsider[1:], avail - nextItem[1])
		print
		withVal += nextItem[0]
		withoutVal, withoutToTake = DTImplicit(toConsider[1:], avail)
		print '    withVal: ', withVal, '  withToTake: ', withToTake
		print '    withoutVal: ', withoutVal, '  withoutToTake: ', withoutToTake
		if withVal > withoutVal:
			print '    withVal > withoutVal'
			result = (withVal, withToTake + (nextItem,))
		else:
			print '    withVal < withoutVal'
			result = (withoutVal, withoutToTake)
	print '<--- outside DTImplicit ', visited
	return result
