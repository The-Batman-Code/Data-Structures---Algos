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


new_queue = Queue()
new_queue.enqueue(2)
new_queue.enqueue(3)
new_queue.enqueue(4)
new_queue.enqueue(5)
new_queue.enqueue(6)
print(new_queue)
print(new_queue.dequeue())
print(new_queue)
print(new_queue.peek())
new_queue.delete()
print(new_queue)
