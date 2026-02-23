"""
Problem: Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000
"""

def myPow(x, n):
    # Recursive helper function that always uses a positive power 'n'.
    def helper(x, n):
        # Base case 1: 0 to any power is 0.
        if x == 0:
            return 0
        # Base case 2: Any number to the power of 0 is 1.
        if n == 0:
            return 1
            
        # Optimization (Fast Power Algorithm):
        # Instead of multiplying 'x' by itself 'n' times (O(n)),
        # we calculate x^(n/2) once...
        res = helper(x, n // 2)
        # ...and square it! x^n = x^(n/2) * x^(n/2). This reduces time to O(log n).
        res = res * res
        
        # If 'n' was ODD, an integer division rounded down, so we are missing one 'x'.
        # Multiply by 'x' one last time to fix it! 
        # (e.g., x^5 = x^2 * x^2 * x)
        return x * res if n % 2 else res
        
    # We call our helper function enforcing a strictly positive 'n'.
    res = helper(x, abs(n))
    
    # If the original 'n' was negative, the mathematical result is just 1 divided by the positive result.
    # (e.g., 2^-3 = 1 / 2^3)
    return res if n >= 0 else 1 / res

if __name__ == "__main__":
    x = 2.00000
    n = 10
    print(f"Input: x = {x}, n = {n}")
    print(f"Output: {myPow(x, n)}")
