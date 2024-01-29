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

    def searchNode(self, key):
        for i in range(len(self.customList)):  # This takes O(n) TC
            if self.customList[i] == key:
                return "Success"
        return "Not Found"

    # TC and SC of the above method is O(n) and O(1) respectively

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return None
        print(self.customList[index])
        self.preOrderTraversal(index * 2)  # This takes O(n/2) TC
        self.preOrderTraversal(index * 2 + 1)  # This takes O(n/2) TC

    # TC and SC of the above method is O(n)


newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
print(newBT.searchNode("Hot"))
newBT.preOrderTraversal(1)
