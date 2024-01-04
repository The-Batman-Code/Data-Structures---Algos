class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return "\n".join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            False

    # TC and SC of the above method is O(1)

    def push(self, value):
        new_node = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = new_node
            return True
        else:
            new_node.next = self.LinkedList.head
            self.LinkedList.head = new_node
            return True
    # TC and SC of the above method is O(1)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            value = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return value
    # TC and SC of the above method is O(1)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            value = self.LinkedList.head.value
            return value
    # TC and SC of the above method is O(1)

    def delete(self):
        if self.isEmpty():
            return None
        else:
            self.LinkedList.head = None
            return True
    # TC and SC of the above method is O(1)


new_stack = Stack()
print(new_stack.isEmpty())
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.push(4)
new_stack.push(5)
print(new_stack)
new_stack.pop()
print("-----------")
print(new_stack)
print(new_stack.peek())
