"""
Problem: Sum of Two Integers
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3
"""

def getSum(a, b):
    # Python handles integers with arbitrary precision, so it doesn't naturally wrap around
    # at 32 bits like C++ or Java. We use a mask to manually force 32-bit behavior.
    mask = 0xFFFFFFFF
    
    # We use bitwise operations to simulate binary addition.
    # We continue until there is no 'carry' left to add (b becomes 0).
    while (b & mask) > 0:
        # Step 1: Find the CARRY
        # The '&' (AND) operator finds bits where BOTH 'a' and 'b' are 1.
        # These are the positions that will generate a carry.
        # We then shift left '<< 1' because a carry affects the *next* higher bit position.
        carry = (a & b) << 1
        
        # Step 2: ADD without carry
        # The '^' (XOR) operator adds bits. If one is 1 and the other 0, the sum is 1.
        # If both are 1, it becomes 0 (the carry handles the overflow).
        a = a ^ b
        
        # Step 3: Prepare the carry for the next iteration to be added to our new 'a'
        b = carry
        
    # Python negative numbers have infinite leading 1s. 
    # If the 32nd bit of our result is a 1 (meaning it should be negative), 
    # we have to convert it back to Python's negative format if 'a' has exceeded max 32-bit bound.
    return (a & mask) if b > 0 else a

if __name__ == "__main__":
    a = 1
    b = 2
    print(f"Input: a = {a}, b = {b}")
    print(f"Output: {getSum(a, b)}")
