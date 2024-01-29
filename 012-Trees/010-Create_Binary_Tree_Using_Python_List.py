class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    # TC of the above method is O(1). SC is O(n) as we will initialize an array of the size of the binary tree


newBT = BinaryTree(8)
