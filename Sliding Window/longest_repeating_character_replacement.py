"""
Problem: Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
"""

def characterReplacement(s, k):
    # Hash Map to track the frequencies of every character inside our Sliding Window.
    count = {}
    res = 0
    # 'l' is our Left pointer, representing the start of the window.
    l = 0
    # 'maxf' keeps track of the single Most Frequent Character count in the current window.
    maxf = 0
    
    # 'r' is our Right pointer expanding the window.
    for r in range(len(s)):
        # 1. Add the new character 's[r]' to our frequency map.
        count[s[r]] = 1 + count.get(s[r], 0)
        
        # 2. Update our global maximum frequency dynamically.
        maxf = max(maxf, count[s[r]])
        
        # Core Formula: (Total Window Length) - (Most Frequent Character Count) = Characters we MUST Replace!
        # If the number of characters we mathematically MUST replace exceeds our allowed 'k' limit:
        # Our window is officially invalid! We must shrink it from the left!
        while (r - l + 1) - maxf > k:
            # We are sliding the left pointer forward, so we must remove the left character's count.
            count[s[l]] -= 1
            l += 1
            
        # If we reach here, our window is mathematically valid (valid replacements <= k).
        # We record the biggest valid window length we've legitimately seen.
        res = max(res, r - l + 1)
        
    return res

if __name__ == "__main__":
    s = "ABAB"
    k = 2
    print(f"Input: s = '{s}', k = {k}")
    print(f"Output: {characterReplacement(s, k)}")
