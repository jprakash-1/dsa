"""
Problem: Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Example 1:
Input: x = 123
Output: 321
"""
import math

def reverse(x):
    # Setup 32-bit signed integer limits
    MIN = -2147483648  # -2^31
    MAX = 2147483647   #  2^31 - 1
    
    res = 0
    # Loop until x becomes 0
    while x:
        # Get the rightmost digit. We use math.fmod because Python's default % operator 
        # behaves strangely with negative numbers (e.g., -1 % 10 = 9, but fmod(-1, 10) = -1.0)
        digit = int(math.fmod(x, 10))  
        
        # Remove the rightmost digit from x. Use int() to truncate towards zero.
        x = int(x / 10)
        
        # OVERFLOW CHECK FOR POSITIVE NUMBERS:
        # If 'res' is already bigger than MAX/10, multiplying by 10 will definitely overflow.
        # If 'res' is EXACTLY MAX/10, we can only add a digit up to 7 (since MAX ends in 7).
        if (res > MAX // 10) or (res == MAX // 10 and digit >= MAX % 10):
            return 0
            
        # OVERFLOW CHECK FOR NEGATIVE NUMBERS:
        # Similar logic, checking against the MIN boundary (ends in 8).
        if (res < int(MIN / 10)) or (res == int(MIN / 10) and digit <= int(math.fmod(MIN, 10))):
            return 0
            
        # If no overflow, safely append the digit to our reversed result.
        res = (res * 10) + digit
        
    return res

if __name__ == "__main__":
    x = 123
    print(f"Input: x = {x}")
    print(f"Output: {reverse(x)}")
