class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    # TC of the above method is O(1) and SC is also O(1)
