"""
Problem: Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]
"""

class MinStack:
    def __init__(self):
        # 'stack' acts as a normal python list stack.
        self.stack = []
        # 'minStack' is our secret weapon to find the minimum in O(1) time!
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # We push the current mathematical minimum at this exact level to minStack.
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        # When we pop the main stack, we safely pop the tracking stack too!
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # The lowest value will always be resting at the top of our tracking stack!
        return self.minStack[-1]

if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(f"getMin: {obj.getMin()}")
    obj.pop()
    print(f"top: {obj.top()}")
    print(f"getMin: {obj.getMin()}")
