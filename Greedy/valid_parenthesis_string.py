"""
Problem: Valid Parenthesis String
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
'*' could be treated as a single right parenthesis ')', a single left parenthesis '(', or an empty string "".

Example 1:
Input: s = "(*))"
Output: true
"""

def checkValidString(s):
    # Because '*' is wild, we don't have a single count of open parentheses.
    # We maintain a RANGE of possible open parentheses counts: [leftMin, leftMax]
    leftMin, leftMax = 0, 0
    
    for c in s:
        # If it's a left parenthesis, both our minimum and maximum possible counts increase.
        if c == "(":
            leftMin, leftMax = leftMin + 1, leftMax + 1
        # If it's a right parenthesis, both counts decrease.
        elif c == ")":
            leftMin, leftMax = leftMin - 1, leftMax - 1
        # If it's a wildcard '*', it could be ')', '', or '('.
        # So our minimum decreases (if we treat it as ')'), 
        # and our maximum increases (if we treat it as '(').
        else:
            leftMin, leftMax = leftMin - 1, leftMax + 1
            
        # If even our MAXIMUM possible open count dips below 0, it means we have 
        # too many ')' that cannot possibly be matched. The string is permanently invalid.
        if leftMax < 0:
            return False
            
        # If our minimum dips below 0, it just means we tried treating too many '*' as ')'.
        # That specific choice is invalid, so we reset the minimum back to 0.
        if leftMin < 0:
            leftMin = 0
            
    # At the end, if 0 is within our valid range of open parentheses (leftMin == 0), 
    # it means there is at least one valid combination that perfectly balances the string!
    return leftMin == 0

if __name__ == "__main__":
    s = "(*))"
    print(f"Input: s = '{s}'")
    print(f"Output: {checkValidString(s)}")
