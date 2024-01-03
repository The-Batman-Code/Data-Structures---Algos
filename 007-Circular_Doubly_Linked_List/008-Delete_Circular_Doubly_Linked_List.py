class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    # TC and SC of this method is O(1)

    def __str__(self):
        return str(self.value)


class DCLinkedList:
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
            if temp == self.head:
                break
            result += " <-> "
        return result

    def append(self, value):  # Here edge case is when there is no node
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length += 1
        # TC and SC of the above method is O(1)

    def prepend(self, value):  # Here edge case is when there is no node
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
            new_node.prev = self.tail
        self.length += 1
        # TC and SC of the above method is O(1)

    def insert(self, value, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.prepend(value)
        elif index == self.length - 1:
            self.append(value)
        else:
            new_node = Node(value)
            temp_node = self.head
            for _ in range(index - 1):  # For loop has O(n) TC
                temp_node = temp_node.next
            temp_node.next.prev = new_node
            new_node.next = temp_node.next
            temp_node.next = new_node
            new_node.prev = temp_node
        self.length += 1

    # TC and SC of the above method is O(n) and O(1) respectively

    def traverse(self):  # Here edge case is when there is no node
        if self.head is None:
            return None
        else:
            temp = self.head
            while temp is not None:  # TC of while loop is O(n)
                print(temp.value)
                temp = temp.next
                if temp == self.head:
                    break

    # TC and SC of the above method is O(n) and O(1) respectively

    def reverse_traverse(self):
        if self.tail is None:
            return None
        else:
            temp = self.tail
            while temp is not None:  # TC of while loop is O(n)
                print(temp.value)
                temp = temp.prev
                if temp == self.tail:
                    break

    # TC and SC of the above method is O(n) and O(1) respectively

    def search(self, value):
        if self.head is None:
            return None
        else:
            temp_node = self.head
            while temp_node:  # This takes O(n) TC
                if temp_node.value == value:
                    return temp_node.value
                if temp_node == self.tail:
                    return None
                temp_node = temp_node.next

    # TC and SC of the above method is O(n) and O(1) respectively

    def delete(self, index):
        if self.head is None:
            return None
        else:
            if index == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif index == self.length - 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                temp = self.head
                for _ in range(index - 1):  # This take O(n) TC
                    temp = temp.next
                temp.next = temp.next.next
                temp.next.next.prev = temp
        self.length -= 1

    # TC of the above method is O(n) and SC is O(1)

    def remove_all(self):
        if self.head is None:
            return None
        else:
            self.tail.next = None
            self.head.prev = None
            temp = self.head
            while temp:  # TC of while loop is O(n)
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None
        return True

    # TC and SC of the above method is O(n) and O(1) respectively


new_dcs_linked_list = DCLinkedList()
new_dcs_linked_list.append(10)
new_dcs_linked_list.append(89)
new_dcs_linked_list.append(14)
new_dcs_linked_list.append(56)
new_dcs_linked_list.append(23)
new_dcs_linked_list.append(45)
print(new_dcs_linked_list)
print(new_dcs_linked_list.head.prev)
new_dcs_linked_list.insert(69, 2)
print(new_dcs_linked_list)
new_dcs_linked_list.traverse()
new_dcs_linked_list.reverse_traverse()
print(new_dcs_linked_list.search(0))
new_dcs_linked_list.delete(5)
print(new_dcs_linked_list)
new_dcs_linked_list.remove_all()
print(new_dcs_linked_list)
