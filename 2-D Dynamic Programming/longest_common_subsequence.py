"""
Problem: Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
"""

def longestCommonSubsequence(text1, text2):
    # Create a 2D DP grid initialized with zeros.
    # The grid dimensions are slightly larger (+1) than the strings to handle 
    # the base cases where one or both remaining strings are empty (length 0).
    dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    # We iterate backwards through both strings (Bottom-Up Dynamic Programming approach)
    # i tracks characters in text1, j tracks characters in text2
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            # Scenario 1: The characters MATCH!
            if text1[i] == text2[j]:
                # We add 1 to our subsequence length, and then we look DIAGONALLY 
                # (dp[i+1][j+1]) to see the longest subsequence for the *remaining* parts of both strings.
                dp[i][j] = 1 + dp[i + 1][j + 1]
                
            # Scenario 2: The characters DO NOT match.
            else:
                # We can't include both characters. We must skip one.
                # Do we skip text1's character (go down, dp[i+1][j]) 
                # OR text2's character (go right, dp[i][j+1])?
                # We take the MAXIMUM result of those two choices.
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    # The top-left cell will contain the result for evaluating both FULL strings from index 0.
    return dp[0][0]

if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    print(f"Input: text1 = '{text1}', text2 = '{text2}'")
    print(f"Output: {longestCommonSubsequence(text1, text2)}")
