"""
Problem: Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
"""

def partition(s):
    res = []
    part = [] # This list will hold our current sequence of valid palindromes.
    
    # Depth-First Search for Exploring Partitions
    # 'i' represents the starting index of the substring we are currently evaluating.
    def dfs(i):
        # Base Case: If we've reached the end of the string, it means our current 'part'
        # list contains a valid full partitioning of 's'.
        if i >= len(s):
            res.append(part.copy())
            return
            
        # Explore all possible substrings starting at 'i' and ending at 'j'.
        for j in range(i, len(s)):
            # CHECK: Is the current substring s[i : j + 1] a palindrome?
            if isPali(s, i, j):
                # 1. It IS a palindrome! Add it to our current partition list.
                part.append(s[i : j + 1])
                
                # 2. Recursively find partitions for the REST of the string (starting at j+1).
                dfs(j + 1)
                
                # 3. BACKTRACK: Remove the last palindrome to try a different, 
                # potentially longer palindrome ending further down.
                part.pop()
                
    # Helper Function: Checks if a string segment is a palindrome using two pointers.
    def isPali(s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
        
    # Start DFS at index 0.
    dfs(0)
    return res

if __name__ == "__main__":
    s = "aab"
    print(f"Input: s = '{s}'")
    print(f"Output: {partition(s)}")
