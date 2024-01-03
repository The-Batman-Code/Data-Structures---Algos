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

    def nthtolast(self, n):
        pointer1 = self.head
        pointer2 = self.head

        for _ in range(n):  # TC of for loop is O(n)
            if pointer2 is None:
                return None
            pointer2 = pointer2.next
        while pointer2:  # TC of while loop is O(n)
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1

    # TC of the above method is O(n) and SC is O(1)


list = LinkedList()
list.head = Node(2)
list.head.next = Node(2)
list.head.next.next = Node(2)
list.head.next.next.next = Node(2)
list.head.next.next.next.next = Node(3)
list.head.next.next.next.next.next = Node(2)
list.head.next.next.next.next.next.next = Node(5)
print(list)
print(list.nthtolast(0).value)
