"""
Problem: Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""

def merge(intervals):
    # Sort the intervals based strictly on their START times.
    intervals.sort(key=lambda pair: pair[0])
    
    # Initialize the output list with the very first interval.
    output = [intervals[0]]

    # Iterate through the rest of the sorted intervals.
    for start, end in intervals:
        # Get the END time of the MOST RECENTLY added interval in our output list.
        lastEnd = output[-1][1]

        # Check for OVERLAP: If the current interval starts before or exactly when 
        # the last added interval ends, they overlap!
        if start <= lastEnd:
            # Merge them by extending the end time of the last added interval.
            # We take the max because the current interval might be completely 
            # swallowed by the last one (e.g., merging [1,5] with [2,3]).
            output[-1][1] = max(lastEnd, end)
            
        # No overlap! They are distinct intervals.
        else:
            # Just append the current interval to the output normally.
            output.append([start, end])
            
    return output

if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Input: intervals = {intervals}")
    print(f"Output: {merge(intervals)}")
