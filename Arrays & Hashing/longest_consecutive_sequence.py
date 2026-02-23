"""
Problem: Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

def longestConsecutive(nums):
    # Convert our input array into a Hash Set. 
    # Why? Searching for "does this number exist" in an array takes O(N) time.
    # In a Hash Set, looking up a number takes O(1) instant time. This avoids O(N^2) loops!
    numSet = set(nums)
    longest = 0
    
    for n in nums:
        # Core Reasoning: We only want to start counting a sequence from its very beginning.
        # How do we know if 'n' is the start of a sequence?
        # If the number immediately before it (n - 1) is NOT in our set, then 'n' MUST be the start!
        # This clever check prevents us from re-counting sequences repeatedly.
        if (n - 1) not in numSet:
            length = 1
            
            # As long as the *next* consecutive number (n + length) exists in our set,
            # we keep growing our current valid sequence.
            while (n + length) in numSet:
                length += 1
                
            # After the sequence breaks, we see if it was the longest one we've found so far.
            longest = max(longest, length)
            
    return longest

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(f"Input: nums = {nums}")
    print(f"Output: {longestConsecutive(nums)}")
