class Queue:
    def __init__(self):
        self.items = []  # TC and SC is O(1)

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    # TC and SC of the above method is O(n+k)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        # TC and SC of the above method is O(1)

    def enqueue(self, value):
        self.items.append(value)
        return True

    # TC of this method is amortized constant which in worst case can take O(n^2). SC is O(1)

    def dequeue(self):
        if self.isEmpty():
            return False
        else:
            return self.items.pop(
                0
            )  # TC of this pop is O(n) as all elements have to shift left
        # TC and SC of the above method is O(n) and O(1)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[0]
        # TC and SC of the above method is O(1)

    def delete(self):
        self.items = None
        return True

    # TC and SC of the above method is O(1)


new_queue = Queue()
print(new_queue.isEmpty())
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
new_queue.enqueue(4)
new_queue.enqueue(5)
print(new_queue)
new_queue.dequeue()
print(new_queue)
print(new_queue.peek())
new_queue.delete()
print(new_queue)
