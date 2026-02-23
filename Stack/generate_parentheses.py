"""
Problem: Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

def generateParenthesis(n):
    # 'stack' will hold a single valid combination of "(" and ")" as we build it.
    stack = []
    # 'res' will store every complete valid combination we uniquely generate.
    res = []
    
    # We use a Recursive Backtracking technique!
    def backtrack(openN, closedN):
        # Base Case: Our combination is complete when we've used all 'n' pairs.
        if openN == closedN == n:
            res.append("".join(stack))
            return
            
        # Rule 1: We can always add an Open parenthesis if we haven't reached 'n'.
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            # After recursion, we pop it off to backtrack and try other branches!
            stack.pop()
            
        # Rule 2: We can only add a Closed parenthesis if we have more Open ones than Closed ones!
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            # Pop off to gracefully backtrack.
            stack.pop()
            
    # Start the recursive tree with 0 open and 0 closed.
    backtrack(0, 0)
    return res

if __name__ == "__main__":
    n = 3
    print(f"Input: n = {n}")
    print(f"Output: {generateParenthesis(n)}")
