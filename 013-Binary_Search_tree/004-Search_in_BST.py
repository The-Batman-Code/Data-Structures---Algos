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


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # TC and SC of the above method is O(1)


def insertNode(root, value):
    if root.data == None:
        root.data = value
    elif value <= root.data:
        if root.leftChild is None:
            root.leftChild = BSTNode(value)
        else:
            insertNode(root.leftChild, value)  # TC is O(n/2)
    else:
        if root.rightChild is None:
            root.rightChild = BSTNode(value)
        else:
            insertNode(root.rightChild, value)  # TC is O(n/2)
    return "The node has been successfully inserted"


# TC and SC of the above method is O(logN)


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


# TC and SC of the above method is O(n)


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


newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)

# preOrderTraversal(newBST)
# inOrderTraversal(newBST)
# postOrderTraversal(newBST)
# levelOrderTraversal(newBST)

search(newBST, 60)
