class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofstring = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endofstring = True
        print("Success")

    # TC and SC of the above method is O(n) where n is the length of the word
    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        if currentNode.endofstring == True:
            return True
        else:
            return False


# TC of the above method is O(n) where n is the length of the word. SC is O(1).


def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canthisNodebeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)

    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endofstring = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endofstring == True:
        deleteString(currentNode, word, index + 1)
        return False
    canthisNodebeDeleted = deleteString(currentNode, word, index + 1)
    if canthisNodebeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
print(newTrie.searchString("Appl"))
deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("App"))
