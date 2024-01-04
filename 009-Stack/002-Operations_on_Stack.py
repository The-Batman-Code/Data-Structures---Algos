class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values_rev = self.list[::-1]
        values = [str(x) for x in values_rev]
        return "\n".join(values)

    # TC of the above method is O(1) and SC is also O(1)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # TC and SC of the above method is O(1)
    def push(self, value):
        self.list.append(value)
        return True

    # TC of the above method is O(n) as when python needs to allocate new memory it may copy all the elements and delete the previous memory data. SC is O(1)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.list.pop()

    # TC and SC of the above method is O(1)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.list[-1]

    # TC and SC of the above method is O(1)

    def delete(self):
        self.list = None
        return None

    # TC and SC of the above method is O(1)


new_stack = Stack()
print(new_stack.isEmpty())
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.push(4)
new_stack.push(5)
print(new_stack)
print("----------")
print(new_stack.pop())
print("-------")
print(new_stack)
print(new_stack.peek())
print(new_stack.delete())
