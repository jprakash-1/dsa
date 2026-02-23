"""
Problem: Partition Equal Subset Sum
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
"""

def canPartition(nums):
    # If the total sum of the array is odd, we CANNOT split it into two equal halves!
    # (e.g., sum=11, we can't have two subsets summing to 5.5)
    if sum(nums) % 2:
        return False
        
    # 'dp' is a set that will store ALL the possible sums we can create 
    # using different combinations of numbers from our array.
    dp = set()
    dp.add(0) # Base case: we can always make a sum of 0 using 0 elements.
    
    # The target sum we are trying to reach for ONE of the subsets.
    target = sum(nums) // 2
    
    # We iterate backwards through the array, making a choice for each number:
    # Do we include it in our current subset sum, or not?
    for i in range(len(nums) - 1, -1, -1):
        nextDP = set() # Temporary set for the next iteration
        
        for t in dp:
            # Check: if we include the current number in our existing sum 't', 
            # do we perfectly hit our target?
            if (t + nums[i]) == target:
                return True
                
            # Choice 1: INCLUDE the number in the sum
            nextDP.add(t + nums[i])
            # Choice 2: DO NOT include the number (just keep the old sum)
            nextDP.add(t)
            
        # Move to the next number, with our newly updated set of possible sums
        dp = nextDP
        
    # If we evaluated every number and never hit the target, it's impossible.
    return False

if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(f"Input: nums = {nums}")
    print(f"Output: {canPartition(nums)}")
