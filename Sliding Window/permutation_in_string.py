"""
Problem: Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
"""

def checkInclusion(s1, s2):
    # Basic Validation: If s1 is longer than s2, it is impossible for s2 to contain s1.
    if len(s1) > len(s2):
        return False
        
    # We will use two frequency arrays of exactly size 26 (representing 'a' to 'z').
    s1Count, s2Count = [0] * 26, [0] * 26
    
    # 1. Initialize the First Valid Window (size of s1).
    for i in range(len(s1)):
        # ord(char) - ord('a') maps 'a' to 0, 'b' to 1, ..., 'z' to 25.
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1
        
    # 'matches' keeps track of exactly how many alphabet characters have identical frequencies 
    # between our target s1 string and the current active sliding window in s2.
    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)
        
    # 'l' is our Left pointer. 'r' is our Right pointer expanding seamlessly.
    l = 0
    for r in range(len(s1), len(s2)):
        # If all 26 characters exactly match their required frequencies, we found a permutation!
        if matches == 26:
            return True
            
        # --- Slide the Window Right (Add the new rightmost character) ---
        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        # Did adding this character make its frequency perfectly match our target?
        if s1Count[index] == s2Count[index]:
            matches += 1
        # Did adding this character BREAK a previously perfect frequency match?
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1
            
        # --- Slide the Window Left (Remove the old leftmost character) ---
        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        # Did removing this character make its frequency perfectly match our target?
        if s1Count[index] == s2Count[index]:
            matches += 1
        # Did removing this character BREAK a previously perfect frequency match?
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
            
        # Move the left pointer forward officially.
        l += 1
        
    # Final check for the very last window iteration.
    return matches == 26

if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(f"Input: s1 = '{s1}', s2 = '{s2}'")
    print(f"Output: {checkInclusion(s1, s2)}")
