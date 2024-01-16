class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
# TC and SC of the above method is O(1) as we are just initializing


def preOrderTraversal(root):
    if not root:
        return None
    print(root.data)
    preOrderTraversal(root.leftChild)  # TC is O(n/2)
    preOrderTraversal(root.rightChild)  # TC is O(n/2)


# Overall TC of the above method is O(n) and SC is also O(n)


preOrderTraversal(newBT)
