class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return " ".join(values)

    def enqueue(self, value):
        new_node = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node
        else:
            self.linkedlist.tail.next = new_node
            self.linkedlist.tail = new_node

    # TC and SC of the above method is O(1)

    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False

    # TC and SC of the above method is O(1)

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            temp = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return temp

    # TC and SC of the above method is O(1)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return str(self.linkedlist.head.value)

    # TC and SC of the above method is O(1)

    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None

    # TC and SC of the above method is O(1)


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def preOrderTraversal(root):
    if not root:
        return None
    print(root.data)
    preOrderTraversal(root.leftChild)
    preOrderTraversal(root.rightChild)
    # TC and SC of the above method is O(n)


def inOrderTraversal(root):
    if not root:
        return None
    inOrderTraversal(root.leftChild)
    print(root.data)
    inOrderTraversal(root.rightChild)


# TC and SC of the above method is O(n)


def postOrderTraversal(root):
    if not root:
        return None
    postOrderTraversal(root.leftChild)
    postOrderTraversal(root.rightChild)
    print(root.data)


# TC and SC of the above method is O(n)


def levelOrderTraversal(root):
    if not root:
        return None
    else:
        new_queue = Queue()
        new_queue.enqueue(root)
        while not (new_queue.isEmpty()):
            root = new_queue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                new_queue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                new_queue.enqueue(root.value.rightChild)


def search(root, nodeValue):
    if root.data == nodeValue:
        print("The value has been found")
    elif nodeValue < root.data:
        if root.leftChild.data == nodeValue:
            print("The value is found")
        else:
            search(root.leftChild, nodeValue)  # This takes O(n/2) TC
    else:
        if root.rightChild.data == nodeValue:
            print("The value has been found")
        else:
            search(root.rightChild, nodeValue)  # This takes O(n/2) TC


# TC and SC of the above method is O(logN)


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(
        getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)
    )
    newRoot.height = 1 + max(
        getHeight(newRoot.leftChild), getHeight(newRoot.rightChild)
    )
    return newRoot


def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(
        getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)
    )
    newRoot.height = 1 + max(
        getHeight(newRoot.leftChild), getHeight(newRoot.rightChild)
    )
    return newRoot


# TC and SC of both the methods above is O(1)


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(
            rootNode.leftChild, nodeValue
        )  # TC and SC = O(logn)
    else:
        rootNode.rightChild = insertNode(
            rootNode.rightChild, nodeValue
        )  # TC and SC = O(logn)

    rootNode.height = 1 + max(
        getHeight(rootNode.leftChild), getHeight(rootNode.rightChild)
    )
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode


# TC and SC of the above method is O(logn)

newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
levelOrderTraversal(newAVL)
