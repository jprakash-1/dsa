"""
Problem: Evaluate Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""

def evalRPN(tokens):
    # We use a Stack because operations in RPN always apply to the two most recently seen numbers!
    stack = []
    
    for c in tokens:
        # If the token is a mathematical operator, pop the last two numbers and apply it.
        if c == "+":
            # Order doesn't matter for addition.
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            # Order MATTERS for subtraction! The second popped number is actually the first operand.
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            # Order doesn't matter for multiplication.
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            # Order MATTERS for division! The problem also requires truncating toward zero,
            # which python's int() automatically does cleanly.
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            # If it's just a number, convert it to an integer and push it to the stack.
            stack.append(int(c))
            
    # The final remaining number on the stack is our evaluated answer!
    return stack[0]

if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]
    print(f"Input: tokens = {tokens}")
    print(f"Output: {evalRPN(tokens)}")
