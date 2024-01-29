class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    # TC of the above method is O(1). SC is O(n) as we will initialize an array of the size of the binary tree

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "Binary Tree is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    # TC and SC of the above method is O(1)


newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
