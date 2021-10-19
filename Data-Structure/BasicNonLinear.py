# Self implementation of nonlinear data structrue 
# - Binary Tree
# - Binary Heap
# - Grapgh


class BinaryTree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    # insert the left child
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            tmp = BinaryTree(newNode)
            tmp.leftChild = self.leftChild
            self.leftChild = tmp
    
    # insert the right child
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            tmp = BinaryTree(newNode)
            tmp.rightChild = self.rightChild
            self.rightChild = tmp
    
    # get & set
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key

class BinaryHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.perDown(i)
            i -= 1


    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def perDown(self, i):
        while (i * 2) <= self.currentSize:
            mychild = self.minChild(i)
            if self.heapList[i] > self.heapList[mychild]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mychild]
                self.heapList[mychild] = tmp
            i = mychild

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.perDown(1)
        return retval


