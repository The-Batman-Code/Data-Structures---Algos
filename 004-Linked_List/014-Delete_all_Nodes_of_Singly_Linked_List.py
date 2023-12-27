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
        while current is not None:
            if current.value == target:
                return (index, True)
            current = current.next
            index += 1
        return (-1, False)

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(
        self,
    ):  # Edge case here is when we have only one node. In that case we need to set the head and tail both to none. One more edge case is when we have no node
        if self.length == 0:
            return None
        pop_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            return pop_node
        else:
            self.head = self.head.next
            pop_node.next = None
        self.length -= 1
        return pop_node

    # TC of this method is O(1) as all operations take O(1) TC and SC is also O(1) as no extra space is required.

    def pop_last(
        self,
    ):  # Edge cases are when there is only one node and when there is an empty single linked list
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            while (
                temp_node.next is not self.tail
            ):  # TC of this loop O(n) while other operations are constant TC of O(1)
                temp_node = temp_node.next
            temp_node.next = None
            self.tail = temp_node
        self.length -= 1
        return popped_node
        # TC of this method is O(n) due to the loop. SC is O(1) as no extra space is required

    def remove(
        self, index
    ):  # Here the edge cases are removal from index 0, index which is greater than the length of the list, index which is negative, last index which still points to tail
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_last()  # This takes O(n) TC
        prev_node = self.get(index - 1)  # This take O(N) TC
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
        # TC of this method is O(n) as other operations are O(1) TC operations. SC is O(1) as there as no DS that scale with the input size

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    # TC and SC of this operation is O(1)


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
print(newlinkedlist)
print(newlinkedlist.get(1).value)
newlinkedlist.set_value(89, 2)
print(newlinkedlist)
print(newlinkedlist.pop_first().value)
print(newlinkedlist)
newlinkedlist.pop_last()
print(newlinkedlist)
newlinkedlist.remove(1)
print(newlinkedlist)
newlinkedlist.delete_all()
print(newlinkedlist)
