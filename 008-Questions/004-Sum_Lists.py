class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        # Head of list
        self.head = None
        self.length = 0

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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


def sum_list(lla, llb):
    n1 = lla.head
    n2 = llb.head
    carry = 0
    ll = LinkedList()  # We are adding elements here so SC is O(n)

    while n1 or n2:  # TC of while loop is O(n)
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.append(int(result % 10))
        carry = result // 10
    return ll


# TC and SC of the above method is O(n).


list = LinkedList()
list.head = Node(5)
list.head.next = Node(7)
list.head.next.next = Node(2)

list2 = LinkedList()
list2.head = Node(6)
list2.head.next = Node(9)
list2.head.next.next = Node(2)

print(sum_list(list, list2))
