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

    def __str__(self):
        temp = self.head
        result = ""
        while temp is not None:  # TC of while loop is O(n)
            result += str(temp.value)
            temp = temp.next
            if temp is not None:
                result += str(" <-> ")
        return result

    # TC and SC of the above method is O(n) and O(1) respectively

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

    def prepend(self, value):  # Here the edge case is when the linked list is empty
        new_node = Node(value)
        if self.length is None:
            self.head = None
            self.tail = None
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    # The TC and SC of the above moethod is O(1)

    def traverse(self):
        current_node = self.head
        while current_node:  # TC of while loop is O(n)
            print(current_node.value)
            current_node = current_node.next

    # TC of the above method is O(n) and SC is O(1) as no extra space is required

    def reverse_traverse(self):
        current_node = self.tail
        while current_node:  # TC of while loop is O(n)
            print(current_node.value)
            current_node = current_node.prev

    # TC of the above method is O(n) and SC is O(1) as no extra space is required

    def search(self, target):
        current_node = self.head
        index = 0
        while current_node:  # TC of while loop is O(n)
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return -1

    # TC of the above method is O(n) and SC is O(1)


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
print(new_doubly_linked_list)
new_doubly_linked_list.prepend(6969)
print(new_doubly_linked_list)
new_doubly_linked_list.traverse()
new_doubly_linked_list.reverse_traverse()
print(new_doubly_linked_list.search(10))
