"""
Problem: Interleaving String
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
"""

def isInterleave(s1, s2, s3):
    # Quick Check: If lengths don't add up, it's impossible for s3 to be an interleave.
    if len(s1) + len(s2) != len(s3):
        return False

    # Create a 2D DP table.
    # dp[i][j] tells us if s1[i:] and s2[j:] can successfully interleave to form s3[i+j:]
    # We add 1 to lengths to handle the base cases when strings are empty at the end.
    dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
    
    # Base Case: If both s1 and s2 are empty, they perfectly form the empty s3 at the end.
    dp[len(s1)][len(s2)] = True

    # We iterate backwards through both strings (Dynamic Programming bottom-up approach)
    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            
            # Scenario 1: Can we use a character from s1?
            # We check if:
            # 1. We have characters left in s1 (i < len(s1))
            # 2. The character in s1 matches the CURRENT needed character in s3
            # 3. AND the remaining suffix of s1 & s2 can successfully interleave (dp[i+1][j])
            if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                dp[i][j] = True
                
            # Scenario 2: Can we use a character from s2?
            # We do the exact same check, but for s2.
            # Notice we use 'if', not 'elif', because both branches could potentially be true, 
            # and finding *any* valid path sets dp[i][j] to True.
            if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                dp[i][j] = True
                
    # The answer is whether the entire s1 and s2 (starting at index 0,0) can form s3.
    return dp[0][0]

if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(f"Input: s1 = '{s1}', s2 = '{s2}', s3 = '{s3}'")
    print(f"Output: {isInterleave(s1, s2, s3)}")
