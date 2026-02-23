"""
Problem: Non-Overlapping Intervals
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
"""

def eraseOverlapIntervals(intervals):
    # Step 1: Sort all intervals by their START times.
    intervals.sort(key=lambda x: x[0])
    
    # 'res' will count how many intervals we decide to remove.
    res = 0
    # Keep track of the end time of the LAST valid interval we decided to keep.
    prevEnd = intervals[0][1]
    
    # Iterate through all the intervals (skipping the first one, which is our baseline)
    for start, end in intervals[1:]:
        # Case 1: No Overlap!
        if start >= prevEnd:
            # The current interval starts after the previous one finishes.
            # It's an independent, non-overlapping interval. We KEEP it.
            # Update our tracker to the newly kept interval's end time.
            prevEnd = end
            
        # Case 2: OVERLAP detected!
        else:
            # We *must* remove one of them. Which one?
            # GREEDY CHOICE: We remove the one that ends the LATEST. 
            # Why? Because an interval that lingers longer is more likely to cause 
            # even MORE overlaps with future intervals!
            res += 1 # Increment our removal count.
            
            # Update 'prevEnd' to be the minimum end time between the two overlapping intervals.
            # This mathematically represents us "keeping" the one that finishes earliest.
            prevEnd = min(end, prevEnd)
            
    return res

if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(f"Input: intervals = {intervals}")
    print(f"Output: {eraseOverlapIntervals(intervals)}")
