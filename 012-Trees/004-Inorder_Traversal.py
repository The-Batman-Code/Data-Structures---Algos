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


def inOrderTraversal(root):
    if not root:
        return None
    inOrderTraversal(root.leftChild)  # This takes O(n/2) TC
    print(root.data)
    inOrderTraversal(root.rightChild)  # This takes O(n/2) TC


# Overall the above method takes O(n) TC and SC because when we call a function recursively, we need to store the last info in stack


inOrderTraversal(newBT)
