class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()
    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        curNode = self.root
        for chunkLen in range(1, len(word)+1):
                chunk = word[:chunkLen]
                if not chunk in curNode.children:
                        curNode.children[chunk] = TrieNode()
                if chunk == word:
                        curNode.children[chunk].children["__end__"] = "__end__"
                        print("__end__" in curNode.children[chunk].children)
                else:
                        curNode =curNode.children[chunk]
 
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        curNode = self.root
        returnVal = False
        for chunkLen in range(1, len(word)+1):        
                chunk = word[:chunkLen]
                if not chunk in curNode.children:
                        break
                elif (not "__end__" in curNode.children[chunk].children) and chunk==word:
                        break
                elif "__end__" in curNode.children[chunk].children and chunk==word:
                        returnVal = True
                        break
                else:
                        curNode =curNode.children[chunk]
        return returnVal

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        curNode = self.root
        returnVal = False
        for chunkLen in range(1, len(prefix)+1):
                chunk = prefix[:chunkLen]
                if not chunk in curNode.children:
                        break
                if chunk != prefix:
                        curNode = curNode.children[chunk]
                else:
                        returnVal = True
                        break
        return returnVal

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("a")
print(trie.search("a"))
# trie.search("key")
