"""
Problem: Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

def lengthOfLongestSubstring(s):
    # We use a Hash Set to track the characters currently in our active valid window.
    # Looking up a character in a Set takes O(1) instant time!
    charSet = set()
    
    # 'l' is our Left pointer, representing the start of our sliding window.
    l = 0
    res = 0
    
    # 'r' is our Right pointer, dynamically expanding the window step by step to the right.
    for r in range(len(s)):
        # Core Rule: If the new character s[r] is ALREADY in our set, we have a DUPLICATE!
        # This makes our current window mathematically invalid. 
        # To fix it, we must repeatedly shrink our window from the Left until the duplicate is gone.
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
            
        # Our window is guaranteed to be completely valid and unique again!
        # Now we can safely add the new right character to our Set.
        charSet.add(s[r])
        
        # Calculate the length of our current valid window: (right - left + 1)
        # Update our global Maximum if this new window is the biggest we've seen.
        res = max(res, r - l + 1)
        
    return res

if __name__ == "__main__":
    s = "abcabcbb"
    print(f"Input: s = '{s}'")
    print(f"Output: {lengthOfLongestSubstring(s)}")
