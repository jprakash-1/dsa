"""
Problem: Insert Interval
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""

def insert(intervals, newInterval):
    res = []
    
    for i in range(len(intervals)):
        # Case 1: The new interval is strictly BEFORE the current interval.
        # Since 'intervals' is sorted, it will also be before all subsequent intervals!
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            # We can safely just append the rest of the original intervals and return.
            return res + intervals[i:]
            
        # Case 2: The new interval is strictly AFTER the current interval.
        elif newInterval[0] > intervals[i][1]:
            # The current interval is safe to add. The new interval still needs to find its place.
            res.append(intervals[i])
            
        # Case 3: The new interval OVERLAPS with the current interval.
        else:
            # We don't add anything to 'res' yet. Instead, we MUTATE the new interval
            # to encompass BOTH overlapping intervals. 
            # It will essentially "swallow" the current interval.
            newInterval = [
                min(newInterval[0], intervals[i][0]), # The earliest start time
                max(newInterval[1], intervals[i][1]), # The latest end time
            ]
            
    # If we made it through the whole loop, it means the new interval (or the merged 
    # super-interval we created) belongs at the very end.
    res.append(newInterval)
    return res

if __name__ == "__main__":
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(f"Input: intervals = {intervals}, newInterval = {newInterval}")
    print(f"Output: {insert(intervals, newInterval)}")
