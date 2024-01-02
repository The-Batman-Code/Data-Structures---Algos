class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    # TC and SC of this method is O(1)

    def __str__(self):
        return str(self.value)


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):  # Here the edge case is when there is no node
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    # TC and SC of the above method is O(1) as all are O(1) statements and no extra space is required


new_doubly_linked_list = DLinkedList()
new_doubly_linked_list.append(10)
new_doubly_linked_list.append(20)
new_doubly_linked_list.append(45)
new_doubly_linked_list.append(70)
new_doubly_linked_list.append(34)
new_doubly_linked_list.append(89)
new_doubly_linked_list.append(12)
new_doubly_linked_list.append(76)
print(new_doubly_linked_list.tail)
print(new_doubly_linked_list.head)
