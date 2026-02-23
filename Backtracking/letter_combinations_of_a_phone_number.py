"""
Problem: Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

def letterCombinations(digits):
    res = []
    # A simple map translating each digit to its corresponding phone keypad letters.
    digitToChar = {
        "2": "abc", "3": "def",
        "4": "ghi", "5": "jkl", "6": "mno",
        "7": "pqrs", "8": "tuv", "9": "wxyz",
    }
    
    # Backtracking helper. 
    # 'i' is the index of the current digit. 'curStr' is the string built so far.
    def backtrack(i, curStr):
        # Base Case: We've exhausted all digits provided. The string is fully formed!
        if len(curStr) == len(digits):
            res.append(curStr)
            return
            
        # Recursive Step: Try to append EVERY possible character for the CURRENT digit.
        for c in digitToChar[digits[i]]:
            # Pass 'i + 1' to move to the next digit, and firmly append the new character to 'curStr'.
            backtrack(i + 1, curStr + c)
            
    # Edge Case: If the input is completely empty, don't run the backtracking.
    if digits:
        backtrack(0, "")
        
    return res

if __name__ == "__main__":
    digits = "23"
    print(f"Input: digits = '{digits}'")
    print(f"Output: {letterCombinations(digits)}")
