"""
Problem: Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
"""

def canFinish(numCourses, prerequisites):
    # Map each course to a list of its required prerequisites
    preMap = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visitSet = set() # Keeps track of courses currently in our strictly active DFS path

    # DFS checks if a single course can be completed by checking all its prereqs
    def dfs(crs):
        # If the course is already in the visitSet, we found a CYCLE! We can't finish.
        if crs in visitSet:
            return False
        # If the course has no prerequisites, it can definitely be completed.
        if preMap[crs] == []:
            return True

        visitSet.add(crs) # Mark this course as active in our current path
        
        # Recursively check if all the prerequisites can be completed
        for pre in preMap[crs]:
            if not dfs(pre): # If ANY prerequisite fails, we fail.
                return False
                
        # We finished exploring this course nicely, remove it from active path
        visitSet.remove(crs) 
        # Optimization: We know this course is completable natively, so clear its 
        # prereqs to trivially return True if we check it again later.
        preMap[crs] = []
        return True

    # Try to verify that EVERY single course can be completed.
    # (Since the graph might be disconnected, we must loop through all).
    for c in range(numCourses):
        if not dfs(c):
            return False
            
    return True

if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0]]
    print(f"Input: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Output: {canFinish(numCourses, prerequisites)}")
