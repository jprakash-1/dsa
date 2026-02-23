"""
Problem: K Closest Points to Origin
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
"""
import heapq

def kClosest(points, k):
    # A Heap is perfect for finding the 'k' smallest items dynamically.
    minHeap = []
    
    for x, y in points:
        # We calculate the distance squared. (We don't need the square root for comparison).
        dist = (x ** 2) + (y ** 2)
        minHeap.append([dist, x, y])
        
    # Transform our list into a valid Min-Heap.
    heapq.heapify(minHeap)
    
    res = []
    # Pop the top element (the smallest distance) 'k' times!
    for _ in range(k):
        dist, x, y = heapq.heappop(minHeap)
        res.append([x, y])
        
    return res

if __name__ == "__main__":
    points = [[1, 3], [-2, 2]]
    k = 1
    print(f"Input: points = {points}, k = {k}")
    print(f"Output: {kClosest(points, k)}")
