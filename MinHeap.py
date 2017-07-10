
import sys

class MinHeap:
    def __init__(self, maxSize):
        # init arr to store elements
        self.arr = [None for x in range(maxSize + 1)]
        self.size = 0
        self.arr[0] = -sys.maxint

    def parent(self, pos):
        return pos//2

    def leftChild(self, pos):
        return 2*pos

    def rightChild(self, pos):
        return 2*pos + 1

    def isLeaf(self, pos):
        if pos >= self.size // 2 and pos < self.size:
            return True
        return False

    def swap(self, a, b):
        tmp = self.arr[b]
        self.arr[b] = self.arr[a]
        self.arr[a] = tmp


    def printTree(self):
        for x in xrange(1, size // 2):
            print "Parent:", self.arr[x], "l:", self.arr[leftChild(x)], "r:", self.arr[rightChild(x)]


    def heapify(self):
        if isLeaf(pos) is False:
            if (self.arr[self.leftChild(pos)] < self.arr[pos]
                or
                self.arr[self.leftChild(pos)] < self.arr[pos]):

                # left and right sibling does not have necessary relations
                # choose which way to move
                if self.arr[self.leftChild(pos)] < self.arr[self.leftChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.heapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.leftChild(pos))
                    self.heapify(self.leftChild(pos))

    def minHeap(self):
        for x in range(self.size // 2, 0, -1):
            self.heapify(x)

    def insert(self, elem):
        self.size += 1
        self.arr[self.size] = elem
        # move this leaf to up 
        current = self.size

        # this sort can be skipped i guess
        while current > 1:
            if self.arr[self.parent(current)] < self.arr[current]:
                self.swap(self.parent(current), current)
                current = self.parent(current)

    def extractMin(self):
        result = self.arr[1]
        self.arr[1] = self.arr[self.size]
        self.size -= 1
        self.minHeap()
        return result

