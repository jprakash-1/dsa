"""
Problem: Implement Trie (Prefix Tree)
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
Implement the Trie class.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]
"""

class TrieNode:
    def __init__(self):
        # Maps a character to its corresponding child TrieNode.
        # Example: 'a' -> TrieNode, 'b' -> TrieNode
        self.children = {}
        # Boolean to mark if a complete word ends at this specific node.
        self.endOfWord = False

class Trie:
    def __init__(self):
        # The root node is empty and serves as the starting point for all words.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root # Start from the root
        
        # Go through each character in the word we want to insert
        for c in word:
            # If the character path doesn't exist yet, simply create a new node for it!
            if c not in cur.children:
                cur.children[c] = TrieNode()
                
            # Move the 'cur' pointer down to this child node
            cur = cur.children[c]
            
        # After inserting all characters, mark the *very last* node as the end of a valid word.
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        
        # Trace the path of characters down the Trie
        for c in word:
            # If at any point the next character isn't a child, the word doesn't exist.
            if c not in cur.children:
                return False
            cur = cur.children[c]
            
        # We found the path! But is it a full word? Return the 'endOfWord' flag.
        # Example: searching "app" when only "apple" was inserted will return False.
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        # Exactly like 'search', we trace the path of the prefix
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
            
        # If we successfully traced the whole prefix without returning False,
        # it means words starting with this prefix DO exist in the Trie!
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(f"search('apple'): {trie.search('apple')}")
    print(f"search('app'): {trie.search('app')}")
    print(f"startsWith('app'): {trie.startsWith('app')}")
    trie.insert("app")
    print(f"search('app'): {trie.search('app')}")
