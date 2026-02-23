"""
Problem: Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""

def longestPalindrome(s):
    res = ""
    resLen = 0
    
    # We treat every single character (and the space between them) as the potential 
    # "center" of a palindrome, and we expand outward to find its maximum length.
    for i in range(len(s)):
        # --- Check for ODD length palindromes ---
        # Example: "aba". The center is just 'b'.
        l, r = i, i
        # While characters on the left and right match, keep expanding outwards!
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l : r + 1] # Update our longest found palindrome
                resLen = r - l + 1
            l -= 1
            r += 1
            
        # --- Check for EVEN length palindromes ---
        # Example: "abba". The center is *between* the two 'b's.
        l, r = i, i + 1
        # Again, expand outwards as long as they match.
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
            
    return res

if __name__ == "__main__":
    s = "babad"
    print(f"Input: s = '{s}'")
    print(f"Output: {longestPalindrome(s)}")
