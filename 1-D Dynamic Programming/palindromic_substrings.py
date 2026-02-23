"""
Problem: Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
"""

def countSubstrings(s):
    res = 0
    
    # We treat every single character (and the space between them) as the potential 
    # "center" of a palindrome, and we expand outward to find all palindromes centered there.
    for i in range(len(s)):
        # Count all ODD length palindromes centered precisely at character 'i' (e.g., "aba")
        res += countPali(s, i, i)
        
        # Count all EVEN length palindromes centered *between* character 'i' and 'i+1' (e.g., "abba")
        res += countPali(s, i, i + 1)
        
    return res

# Helper function to expand outwards from a given center (l, r)
def countPali(s, l, r):
    res = 0
    # As long as we haven't hit the edges of the string 
    # AND the left character matches the right character...
    while l >= 0 and r < len(s) and s[l] == s[r]:
        res += 1  # We found a valid palindrome! Count it.
        l -= 1    # Expand left pointer outwards
        r += 1    # Expand right pointer outwards
    return res

if __name__ == "__main__":
    s = "abc"
    print(f"Input: s = '{s}'")
    print(f"Output: {countSubstrings(s)}")
