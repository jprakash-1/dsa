"""
Problem: Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
"""

def wordBreak(s, wordDict):
    # dp[i] tells us: "Is it possible to break the substring starting from index 'i' to the end?"
    # We initialize it with False for all indices, except the very end (base case).
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True # Base case: The empty string at the very end is trivially valid.
    
    # We work BACKWARDS from the end of the string.
    for i in range(len(s) - 1, -1, -1):
        # At the current index 'i', we attempt to match every word in our dictionary.
        for w in wordDict:
            # Two conditions must be met for a match:
            # 1. The word 'w' must physically fit inside the remaining string without going out of bounds.
            # 2. The exact slice of the string must actually equal the word 'w'.
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                # If we found a matching word, our ability to solve the rest of the string from index 'i'
                # depends entirely on whether the REMAINING suffix (starting at i + length of word) is solvable.
                dp[i] = dp[i + len(w)]
                
            # Optimization: If we found ANY word that successfully allows us to break the string from index 'i',
            # we can stop checking other words for this specific index 'i'. One valid way is enough!
            if dp[i]:
                break
                
    # Our final answer is whether the entire string (starting at index 0) can be broken down.
    return dp[0]

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(f"Input: s = '{s}', wordDict = {wordDict}")
    print(f"Output: {wordBreak(s, wordDict)}")
