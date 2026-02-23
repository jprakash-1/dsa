"""
Problem: Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

def topKFrequent(nums, k):
    # 'count' will be our Hash Map to store the frequency of each distinct number.
    count = {}
    
    # 'freq' is an array of empty lists (This is a technique called Bucket Sort).
    # Its size is len(nums) + 1 because the maximum possible frequency of *any* element 
    # is the total number of elements in the entire array itself.
    freq = [[] for _ in range(len(nums) + 1)]

    # 1. Count exactly how many times each number appears in O(N).
    for n in nums:
        # dict.get(n, 0) returns the current count safely, or 0 if it hasn't been seen yet.
        count[n] = count.get(n, 0) + 1
    
    # 2. Group the numbers by their frequency count.
    # Reasoning: If the number '3' appears 2 times, we place '3' into the bucket freq[2].
    for n, c in count.items():
        freq[c].append(n)
        
    # 3. Read the frequency array backwards (from highest frequency to lowest).
    res = []
    for i in range(len(freq) - 1, 0, -1):
        # Add the collected numbers from this frequency bucket to our final result.
        for n in freq[i]:
            res.append(n)
            # If we've collected exactly 'k' elements, our job is completely done!
            if len(res) == k:
                return res
    return res

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {topKFrequent(nums, k)}")
