class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
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
