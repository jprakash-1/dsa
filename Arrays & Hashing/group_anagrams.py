"""
Problem: Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
from collections import defaultdict

def groupAnagrams(strs):
    # We use a defaultdict from the collections module.
    # Why? It automatically creates an empty list if we try to access a key that hasn't been added yet.
    # This saves us from having to write an if-else check for every new key.
    res = defaultdict(list)
    
    # Check every string in our input array one by one
    for s in strs:
        # We create a list of 26 zeros to represent the 26 lowercase English letters.
        # Reasoning: Two words are anagrams if they have the exact same character frequencies.
        # Instead of sorting the string (which takes extra time), counting characters is faster.
        count = [0] * 26
        
        # Iterate over every character 'c' in the current string 's'
        for c in s:
            # ord(c) gives the ASCII integer value of the character.
            # ord('a') is 97. So ord('a') - ord('a') = 0, ord('b') - ord('a') = 1, etc.
            # This perfectly maps 'a' to index 0, 'b' to index 1, up to 'z' at index 25.
            count[ord(c) - ord('a')] += 1
            
        # In Python, lists cannot be used as dictionary keys because they can be changed (mutable).
        # We convert our frequency list into a 'tuple', which is locked (immutable) and valid as a key.
        # We then map this specific character count to the original string, grouping it with its anagrams.
        res[tuple(count)].append(s)
        
    # res.values() gives us all the grouped lists of anagrams without the tuple keys.
    # We convert that into a final list to return as our answer.
    return list(res.values())

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(f"Input: {strs}")
    print(f"Output: {groupAnagrams(strs)}")
