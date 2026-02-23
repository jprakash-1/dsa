"""
Problem: Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
"""

def twoSum(numbers, target):
    # We use two pointers: one starting at the very beginning (left) and one at the very end (right).
    l, r = 0, len(numbers) - 1
    
    # As long as the pointers haven't crossed each other vertically...
    while l < r:
        # Calculate the temporary sum of the two numbers at our current pointers.
        curSum = numbers[l] + numbers[r]
        
        # Reasoning: Since the array is completely SORTED in ascending order:
        # If our total is too BIG, the only mathematical way to make it smaller is to move our right pointer to the left.
        if curSum > target:
            r -= 1
        # Conversely, if our total is too SMALL, we must mechanically increase it by moving our left pointer to the right.
        elif curSum < target:
            l += 1
        # If it exactly securely equals our target, we found the pair!
        else:
            # The problem asks specifically for 1-indexed positions, so we add 1 to both indexes before returning.
            return [l + 1, r + 1]
            
    return []

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(f"Input: numbers = {numbers}, target = {target}")
    print(f"Output: {twoSum(numbers, target)}")
