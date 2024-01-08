class CircularQueue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    # TC and SC of the above method is O(n)

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    # TC and SC of the above method is O(n)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    # TC and SC of the above method is O(1)

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    # TC and SC of the above method is O(1)

    def enqueue(self, value):
        if self.isFull():
            return None
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return True

    # TC and SC of the above method is O(1)

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
        return firstElement

    # TC and SC of the above method is O(1)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[self.start]

    # TC and SC of the above method is O(1)

    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1

    # TC and SC of the above method is O(1)


new_queue = CircularQueue(4)
print(new_queue.isFull())
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
new_queue.enqueue(4)
print(new_queue)
new_queue.dequeue()
print(new_queue)
