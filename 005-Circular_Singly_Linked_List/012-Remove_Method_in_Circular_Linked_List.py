class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):  # Here edge case is when the CLL is empty
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

        # TC and SC of this method is O(1)

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node.next is not None:  # TC of this loop is O(n)
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += " -> "
        return result

    # TC of the above method is O(n) and SC is O(1) as no extra sapce is required

    def prepend(self, value):  # Here edge case is when the CLL is empty
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    # TC and SC of the above method is O(1) as all operations take O(1) time and space

    def insert(
        self, index, value
    ):  # Edge cases here are insertion at the beginning, when circular linked list is empty, when insertion is at the end of the CLL and when the index is greater than the length of the CLL
        new_node = Node(value)
        if index > self.length or index < 0:
            raise Exception("Index out of range")
        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(
                index - 1
            ):  # This loop takes O(n) TC while all other operations take O(1) TC
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        # TC of the above method is O(n) while the SC is O(1) as no extra space is required

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    # TC of this method is O(n) due to the for loop and SC is O(1) as no extra space is required

    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
            if current is self.head:
                break
        return False

    # TC of this method is O(n) due to the while loop and SC is O(1) as no extra space is required

    def get(
        self, index
    ):  # Edge case here is that when the index is negative or too big that we traverse the linked list multiple times
        if index == -1:
            return self.tail
        elif index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    # TC of the above method is O(n) due to the for loop and SC is O(1) as no extra space is required

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # TC of this method is O(n) due to get method and SC is O(1) as no extra space is required

    def pop_first(
        self,
    ):  # Here edge cases are when we have one element and when we have no element
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
            self.length -= 1
        return popped_node

    # TC and SC of the above method is O(1)

    def pop_last(
        self,
    ):  # Here edge case is when we have one element in the list and no element in the list
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:  # While loop takes O(n) TC
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
        self.length -= 1
        return popped_node

    # TC of the above method is O(n) due to the for loop and SC is O(1) as no extra space is required

    def remove(
        self, index
    ):  # Here edge cases are when the index is negative or greater than the size of the linked list, when we want to remove the first elemnt of the list
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop_last()  # This takes O(n) TC
        prev_node = self.get(index - 1)  # This takes O(n) TC
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    # TC of the above method is O(n) and SC is O(1) as no extra space is required


new_cs_linked_list = CSLinkedList()
new_cs_linked_list.append(10)
new_cs_linked_list.append(60)
new_cs_linked_list.append(40)
new_cs_linked_list.append(30)
new_cs_linked_list.append(80)
new_cs_linked_list.append(90)
print(new_cs_linked_list.head.value)
print(new_cs_linked_list.head.next.value)
print(new_cs_linked_list.tail.value)
print(new_cs_linked_list)
new_cs_linked_list.prepend(69)
print(new_cs_linked_list)
new_cs_linked_list.insert(2, 699)
print(new_cs_linked_list)
new_cs_linked_list.traverse()
print(new_cs_linked_list.search(996))
print(new_cs_linked_list.get(3).value)
new_cs_linked_list.set(-1, 100)
print(new_cs_linked_list)
print(new_cs_linked_list.pop_first().value)
print(new_cs_linked_list.pop_last().value)
print(new_cs_linked_list)
new_cs_linked_list.remove(5)
print(new_cs_linked_list)
