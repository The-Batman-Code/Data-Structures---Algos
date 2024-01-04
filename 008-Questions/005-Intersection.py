from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return " -> ".join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


def intersection(lla, llb):
    if lla.tail is not llb.tail:
        return None

    lena = len(lla)
    lenb = len(llb)

    shorter = lla if lena < lenb else llb
    longer = llb if lena < lenb else lla

    diff = len(longer) - len(shorter)
    longer_node = longer.head
    shorter_node = shorter.head

    for _ in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


# TC of the above method is O(A+B) because we have to traverse the whole list to find the length and SC is O(1)


def addSameNode(lla, llb, value):
    tempNode = Node(value)
    lla.tail.next = tempNode
    lla.tail = tempNode
    llb.tail.next = tempNode
    llb.tail = tempNode


lla = LinkedList()
lla.generate(3, 0, 10)

llb = LinkedList()
llb.generate(4, 0, 10)

addSameNode(lla, llb, 11)
addSameNode(lla, llb, 14)

print(lla)
print(llb)
print(intersection(lla, llb))
