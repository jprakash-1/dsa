"""
Problem: Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
"""

def checkInclusion(s1: str, s2: str) -> bool:
    m, n = len(s1), len(s2)
    if m > n:
        return False

    s1_freq = Counter(s1)
    s2_freq = Counter()
    start = 0

    for end in range(n):
        # add current char
        s2_freq[s2[end]] += 1

        # shrink if window too large
        if end - start + 1 > m:
            left_char = s2[start]
            s2_freq[left_char] -= 1
            if s2_freq[left_char] == 0:
                del s2_freq[left_char]
            start += 1

        # compare only when window size == m
        if end - start + 1 == m and s2_freq == s1_freq:
            return True

    return False
    
if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(f"Input: s1 = '{s1}', s2 = '{s2}'")
    print(f"Output: {checkInclusion(s1, s2)}")
