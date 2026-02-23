"""
Problem: Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
"""

def multiply(num1, num2):
    # Edge case: anything multiplied by 0 is 0.
    if "0" in [num1, num2]:
        return "0"
        
    # The maximum possible length of the product string is the sum of their lengths.
    res = [0] * (len(num1) + len(num2))
    
    # We reverse Both strings to make calculating places (ones, tens, hundreds) easier.
    # index 0 is now the ones place, index 1 is tens, etc.
    num1, num2 = num1[::-1], num2[::-1]
    
    # Standard elementary school multiplication algorithm!
    for i1 in range(len(num1)):
        for i2 in range(len(num2)):
            # Multiply single digits
            digit = int(num1[i1]) * int(num2[i2])
            
            # The current place we are adding to in the result is (i1 + i2)
            res[i1 + i2] += digit
            
            # Handle the carry! Add the 'tens' part of the result to the NEXT place value (i1 + i2 + 1)
            res[i1 + i2 + 1] += (res[i1 + i2] // 10)
            
            # Keep only the 'ones' part in the current place value
            res[i1 + i2] = res[i1 + i2] % 10
            
    # Reverse the result back to standard readable format
    res, beg = res[::-1], 0
    
    # Strip any leading zeros that might have been left over at the front of our array
    while beg < len(res) and res[beg] == 0:
        beg += 1
        
    # Convert the integer array back to a single joined string
    res = map(str, res[beg:])
    return "".join(res)

if __name__ == "__main__":
    num1 = "2"
    num2 = "3"
    print(f"Input: num1 = '{num1}', num2 = '{num2}'")
    print(f"Output: {multiply(num1, num2)}")
