"""
Problem: Detect Squares
You are given a stream of points on the X-Y plane. Design an algorithm that:
Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.

Example 1:
Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]
"""
import collections

class DetectSquares:
    def __init__(self):
        # Maps a specific point (x, y) to how many times we've seen it.
        # This handles the requirement that duplicate points are treated distinctly.
        self.ptsCount = collections.defaultdict(int)
        # Keeps a raw list of all points added, so we can iterate over them later.
        self.pts = []

    def add(self, point) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point) -> int:
        res = 0
        px, py = point
        
        # We iterate through every single point we currently have saved.
        # We will magically treat EACH saved point as the DIAGONAL opposite corner to our query point 'point'.
        for x, y in self.pts:
            # How do we know if it's a valid diagonal corner of a square?
            # 1. The X distance must equal the Y distance (abs(py - y) != abs(px - x)). If not, it's a rectangle, not a square.
            # 2. The area must be positive (x == px or y == py means it's just a line, area is 0).
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
                
            # If (x, y) is a valid diagonal corner, we now need to find if the OTHER TWO 
            # essential corners exist in our data structure to complete the square!
            # The other two corners will ALWAYS be at coordinates: (x, py) and (px, y).
            
            # We multiply the counts. 
            # E.g., If we have 2 points at corner A, and 3 points at corner B, 
            # there are 2 * 3 = 6 distinct ways to form the square using those specific locations.
            # (Note: self.ptsCount returns 0 automatically if the point doesn't exist, which beautifully zeros out 'res').
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
            
        return res

if __name__ == "__main__":
    obj = DetectSquares()
    obj.add([3, 10])
    obj.add([11, 2])
    obj.add([3, 2])
    print(f"count([11, 10]): {obj.count([11, 10])}")
