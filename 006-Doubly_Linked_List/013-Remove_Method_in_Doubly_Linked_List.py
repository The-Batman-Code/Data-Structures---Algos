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

    def get(
        self, index
    ):  # Here the edge cases are negtive index and when the index is more than the length of the list
        if index < 0 or index > self.length:
            return None
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):  # TC of this loop is O(n/2)
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):  # TC of this loop is O(n/2)
                current_node = current_node.prev
        return current_node

    # TC of the above method is O(n) and SC is O(1) as no extra space is required

    def set_value(self, index, value):
        current_node = self.get(index)  # TC of get method is O(n)
        if current_node:
            current_node.value = value
            return True
        return False

    # TC of the above method is O(n) and SC is O(1)

    def insert(
        self, index, value
    ):  # Here the edge case is when we want to insert at the beginning, at the end of the list, negative index and index greater than the length of the list
        if index < 0 or index > self.length:
            print("Index out of bounds")
            return
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        temp_node = self.get(
            index - 1
        )  # The get method takes O(n) TC while all others take O(1)
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1

    # TC of the above method is O(n) and SC is O(1) as there is no extra space needed

    def pop_first(
        self,
    ):  # Here edge cases are empty list and one element present in the list
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node
        # TC of the above method is O(1) and SC is also O(1)

    def pop_last(
        self,
    ):  # Here the edge case is when there is no element in the list and when there is one element in the list
        if not self.head:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            popped_node.prev = None
            self.tail.next = None
        self.length -= 1
        return popped_node

    # TC of the above method is O(1) and SC is also O(1)

    def remove(
        self, index
    ):  # Here the edge cases are when the index is 0, the last index, when the index is greater than the length of the list and when the index is negative
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_last()
        popped_node = self.get(index)  # The get method takes O(n) TC
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1
        return popped_node

    # TC of the above method is O(n) and SC is also O(1)


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
print(new_doubly_linked_list.get(5))
new_doubly_linked_list.set_value(5, 1)
print(new_doubly_linked_list)
new_doubly_linked_list.insert(7, 0)
print(new_doubly_linked_list)
new_doubly_linked_list.pop_first()
print(new_doubly_linked_list)
new_doubly_linked_list.pop_last()
print(new_doubly_linked_list)
new_doubly_linked_list.remove(5)
print(new_doubly_linked_list)
