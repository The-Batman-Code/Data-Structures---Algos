class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # TC and SC of this method is O(1)


cslinkedlist = CSLinkedList(10)
print(cslinkedlist.head.value)
