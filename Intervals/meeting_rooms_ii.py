"""
Problem: Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
"""

def minMeetingRooms(intervals):
    # Separate the start times and end times into two independent sorted lists.
    # We just need to track the chronological flow of time (when a meeting starts vs ends),
    # regardless of which specific meeting it is.
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])

    res, count = 0, 0
    s, e = 0, 0
    
    # We iterate chronologically through all the meetings.
    while s < len(intervals):
        # Did a meeting START before the next available meeting room ENDED?
        if start[s] < end[e]:
            # Yes! We need to allocate a NEW room.
            s += 1
            count += 1
            
        # Or did a meeting END before the next meeting started?
        else:
            # A meeting finished! This frees up an existing room.
            e += 1
            count -= 1
            
        # Keep track of the maximum number of simultaneous rooms we needed at any point.
        res = max(res, count)
        
    return res

if __name__ == "__main__":
    intervals = [(0, 30), (5, 10), (15, 20)]
    print(f"Input: intervals = {intervals}")
    print(f"Output: {minMeetingRooms(intervals)}")
