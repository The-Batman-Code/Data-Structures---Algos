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
