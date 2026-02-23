"""
Problem: Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""

def dailyTemperatures(temperatures):
    # Initialize our result array with 0s. If we never find a warmer day, it stays 0.
    res = [0] * len(temperatures)
    
    # This Stack will store pairs of: [temperature, original_index]
    # It acts as a "Monotonically Decreasing Stack" (temperatures in the stack strictly go down).
    stack = []  
    
    for i, t in enumerate(temperatures):
        # While our stack is not empty AND today's temperature 't' is WARMER 
        # than the temperature at the top of our stack...
        while stack and t > stack[-1][0]:
            # We found a warmer day for the past temperature at the top of the stack!
            stackT, stackInd = stack.pop()
            # The number of days we waited is today's index minus the past day's index.
            res[stackInd] = i - stackInd
            
        # Add today's temperature and index to the stack to wait for a future warmer day.
        stack.append([t, i])
        
    return res

if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"Input: temperatures = {temperatures}")
    print(f"Output: {dailyTemperatures(temperatures)}")
