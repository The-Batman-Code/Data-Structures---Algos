class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofstring = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


# TC and SC of the above methods is O(1)
newTrie = Trie()
