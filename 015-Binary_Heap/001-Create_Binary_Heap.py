class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


# TC and SC of the above method is O(1) and O(n) respectively


def peekofHeap(rootNode):
    if not rootNode:
        return 0
    return rootNode.customList[1]


# TC and SC of the above method is O(1)


def sizeofHeap(rootNode):
    if not rootNode:
        return 0
    return rootNode.heapSize


# TC and SC of the above method is O(1)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return 0
    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.customList[i])


# TC and SC of the above method is O(n) and O(1) resp.

newBinaryHeap = Heap(5)
print(peekofHeap(newBinaryHeap))
print(sizeofHeap(newBinaryHeap))
levelOrderTraversal(newBinaryHeap)
