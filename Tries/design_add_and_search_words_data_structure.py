"""
Problem: Design Add and Search Words Data Structure
Design a data structure that supports adding new words and finding if a string matches any previously added string.
A word could contain the dot character '.' to represent any one letter.

Example 1:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"]]
Output
[null,null,null,null,false,true,true]
"""

class TrieNode:
    def __init__(self):
        # Standard Trie Node setup: children map and endOfWord flag.
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Standard Trie insertion.
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # We need a DFS helper because the '.' character requires us to branch out
        # and check ALL possible children paths at a given node.
        # 'j' is the index in the 'word', 'root' is the current TrieNode we are at.
        def dfs(j, root):
            cur = root
            
            # Start iterating from index 'j' to the end of the word.
            for i in range(j, len(word)):
                c = word[i]
                
                # The tricky part: handling the '.' wildcard character.
                if c == ".":
                    # A '.' can match ANY character. So, we must recursively check 
                    # every single child node of the current node to see if any path matches.
                    for child in cur.children.values():
                        # If ANY recursive DFS call returns True, we have a match!
                        if dfs(i + 1, child):
                            return True
                    # If we checked all children and none worked out, return False.
                    return False
                else:
                    # Regular character matching (no wildcard).
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
                    
            # After processing all characters (or wildcards), are we at the end of a valid word?
            return cur.endOfWord
            
        # Kick off the DFS search from index 0 at the root of the Trie.
        return dfs(0, self.root)

if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(f"search('pad'): {wordDictionary.search('pad')}")
    print(f"search('bad'): {wordDictionary.search('bad')}")
    print(f"search('.ad'): {wordDictionary.search('.ad')}")
