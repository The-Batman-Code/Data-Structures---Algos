class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        # Head of list
        self.head = None

    def __str__(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.value)
            temp = temp.next
            if temp is None:
                break
            result += str(" -> ")
        return result

    def partition(self, x):
        current_node = self.head
        self.tail = self.head

        while current_node:  # TC of while loop is O(n)
            next_node = current_node.next
            current_node.next = None
            if current_node.value < x:
                current_node.next = self.head
                self.head = current_node
            else:
                self.tail.next = current_node
                self.tail = current_node
            current_node = next_node

        if self.tail.next is not None:
            self.tail.next = None
        return self.head

    # TC of the above method is O(n) and SC is O(1)


list = LinkedList()
list.head = Node(5)
list.head.next = Node(7)
list.head.next.next = Node(2)
list.head.next.next.next = Node(9)
list.head.next.next.next.next = Node(3)
list.head.next.next.next.next.next = Node(2)
list.head.next.next.next.next.next.next = Node(8)
print(list)
print(list.partition(5))
print(list)
