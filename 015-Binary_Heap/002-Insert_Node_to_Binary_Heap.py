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


def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            rootNode.customList[parentIndex], rootNode.customList[index] = (
                rootNode.customList[index],
                rootNode.customList[parentIndex],
            )

        heapifyTreeInsert(rootNode, parentIndex, heapType)  # TC and SC = O(logn)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            rootNode.customList[parentIndex], rootNode.customList[index] = (
                rootNode.customList[index],
                rootNode.customList[parentIndex],
            )

        heapifyTreeInsert(rootNode, parentIndex, heapType)  # TC and SC = O(logn)


# TC and SC of the above method is O(logn)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)  # TC and SC is O(logn)
    return "The value has been inserted"


# TC and SC of the above method is O(logn)


newBinaryHeap = Heap(5)
insertNode(newBinaryHeap, 4, "Max")
insertNode(newBinaryHeap, 5, "Max")
insertNode(newBinaryHeap, 2, "Max")
insertNode(newBinaryHeap, 1, "Max")
print(peekofHeap(newBinaryHeap))
print(sizeofHeap(newBinaryHeap))
levelOrderTraversal(newBinaryHeap)
