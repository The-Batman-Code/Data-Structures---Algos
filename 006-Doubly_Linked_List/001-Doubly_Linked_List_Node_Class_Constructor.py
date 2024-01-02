class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    # TC and SC of this method is O(1)

    def __str__(self):
        return str(self.value)


new_node = Node(10)
print(new_node)
