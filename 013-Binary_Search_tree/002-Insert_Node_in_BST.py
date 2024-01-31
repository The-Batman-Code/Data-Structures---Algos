class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # TC and SC of the above method is O(1)


def insertNode(root, value):
    if root.data == None:
        root.data = value
    elif value <= root.data:
        if root.leftChild is None:
            root.leftChild = BSTNode(value)
        else:
            insertNode(root.leftChild, value)  # TC is O(n/2)
    else:
        if root.rightChild is None:
            root.rightChild = BSTNode(value)
        else:
            insertNode(root.rightChild, value)  # TC is O(n/2)
    return "The node has been successfully inserted"


# TC and SC of the above method is O(logN)


newBST = BSTNode(None)
print(insertNode(newBST, 70))
print(insertNode(newBST, 60))
print(newBST.data)
print(newBST.leftChild.data)
