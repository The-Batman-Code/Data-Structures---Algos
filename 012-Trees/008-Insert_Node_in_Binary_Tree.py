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


# new_queue = Queue()
# new_queue.enqueue(2)
# new_queue.enqueue(3)
# new_queue.enqueue(4)
# new_queue.enqueue(5)
# new_queue.enqueue(6)
# print(new_queue)
# print(new_queue.dequeue())
# print(new_queue)
# print(new_queue.peek())
# new_queue.delete()
# print(new_queue)


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
# TC and SC of the above method is O(1) as we are just initializing


def preOrderTraversal(root):
    if not root:
        return None
    print(root.data)
    preOrderTraversal(root.leftChild)  # TC is O(n/2)
    preOrderTraversal(root.rightChild)  # TC is O(n/2)


# Overall TC of the above method is O(n) and SC is also O(n)


def inOrderTraversal(root):
    if not root:
        return None
    inOrderTraversal(root.leftChild)  # This takes O(n/2) TC
    print(root.data)
    inOrderTraversal(root.rightChild)  # This takes O(n/2) TC


# Overall the above method takes O(n) TC and SC because when we call a function recursively, we need to store the last info in stack


def postOrderTraversal(root):
    if not root:
        return None
    postOrderTraversal(root.leftChild)  # This takes O(n/2) TC
    postOrderTraversal(root.rightChild)  # This takes O(n/2) TC
    print(root.data)


# The TC and SC of the above method is O(n)


def levelOrderTraversal(root):
    if not root:
        return None
    else:
        new_queue = Queue()
        new_queue.enqueue(root)
        while not (new_queue.isEmpty()):  # This takes O(n) TC
            root = new_queue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                new_queue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                new_queue.enqueue(root.value.rightChild)
    # TC of the above method is O(n) and SC is also O(n) as we add all elements in Queue


def searchBT(root, nodeValue):
    if not root:
        return None
    else:
        new_queue = Queue()
        new_queue.enqueue(root)
        while not (new_queue.isEmpty()):
            root = new_queue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if root.value.leftChild is not None:
                new_queue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                new_queue.enqueue(root.value.rightChild)
        return "Not Found"
    # TC and SC of the above method is O(n)


def insertNodeBT(root, newNode):
    if not root:
        root = newNode
    else:
        new_queue = Queue()
        new_queue.enqueue(root)
        while not (new_queue.isEmpty()):
            root = new_queue.dequeue()
            if root.value.leftChild is not None:
                new_queue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully Inserted"
            if root.value.rightChild is not None:
                new_queue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully Inserted"
    # TC and SC of the above method is O(n)


new_node = TreeNode("Cola")
print(insertNodeBT(newBT, new_node))
levelOrderTraversal(newBT)
