<<<<<<< HEAD
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


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
print(newTrie.searchString("Appl"))
=======
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


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
print(newTrie.searchString("Appl"))
>>>>>>> eadcd1fb2137b8cfa8a6c5c11b7d36dd4814e3d7
