"""
Problem: Decode Ways
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways).
Given a string s containing only digits, return the number of ways to decode it.

Example 1:
Input: s = "12"
Output: 2
"""

def numDecodings(s):
    # dp tracks the number of ways to decode starting from the current digit
    # dp2 tracks the number of ways starting from the *next* digit
    dp, dp2 = 1, 0
    
    # We iterate backwards through the string, solving smaller subproblems first
    for i in range(len(s) - 1, -1, -1):
        tmp = dp # temporarily store the current 'dp' to become 'dp2' for the next iteration
        
        # Rule 1: A "0" alone CANNOT be decoded. 
        # (There is no mapping for "0", only "10" or "20")
        if s[i] == "0":
            dp = 0
            
        # Rule 2: Can we combine the current digit with the NEXT digit to form a valid letter?
        # A valid 2-digit number is between 10 and 26.
        # This occurs if: current is "1", OR current is "2" and next is "0-6".
        elif i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
            # If we can form a 2-digit number, we add the number of ways we could 
            # decode the rest of the string *after* those two digits (which is stored in dp2).
            dp += dp2
            
        # Shift our historical pointers backwards
        dp2 = tmp
        
    return dp

if __name__ == "__main__":
    s = "12"
    print(f"Input: s = '{s}'")
    print(f"Output: {numDecodings(s)}")
