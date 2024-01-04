class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list[::-1]
        values = [str(x) for x in values]
        return "\n".join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return False
        else:
            self.list.append(value)
            return True

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.list[-1]

    def delete(self):
        self.list = None
        return None


new_stack = Stack(4)
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.push(4)
print(new_stack.push(5))
print(new_stack)
new_stack.pop()
print(new_stack)
