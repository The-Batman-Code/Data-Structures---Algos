class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        index = 0
        while (
            current is not None
        ):  # TC of this while loop is O(n) and other operations is O(1)
            if current.value == target:
                return (index, True)
            current = current.next
            index += 1
        return (-1, False)


# TC of this search method is O(n) due to the for loop while SC is O(1) as no extra space is required to do this operation

newlinkedlist = LinkedList()
newlinkedlist.append(10)
newlinkedlist.append(20)
newlinkedlist.append(30)
print(newlinkedlist)
newlinkedlist.prepend(5)
print(newlinkedlist)
newlinkedlist.insert(1, 69)
newlinkedlist.traverse()
print(newlinkedlist.search(5))
