"""
Problem: Course Schedule II
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
"""

def findOrder(numCourses, prerequisites):
    # Map each course to its list of prerequisites
    prereq = {c: [] for c in range(numCourses)}
    for crs, pre in prerequisites:
        prereq[crs].append(pre)

    output = []
    # 'visit' set: courses we have FULLY completed and added to output
    # 'cycle' set: courses currently in our active recursive DFS path
    visit, cycle = set(), set()

    # DFS function to verify and add a given course to our output
    def dfs(crs):
        # We detected a loop in our prerequisites! E.g. A requires B, and B requires A.
        if crs in cycle:
            return False
            
        # We already processed this course and its prerequisites successfully.
        if crs in visit:
            return True

        # Add course to active cycle path
        cycle.add(crs)
        
        # We must take ALL prerequisites before we can take the current course
        for pre in prereq[crs]:
            if dfs(pre) == False: # If ANY prerequisite cannot be taken, we fail
                return False
                
        # We successfully explored all prerequisites for this course!
        cycle.remove(crs) # Remove from active path
        visit.add(crs)    # Mark as completely finished
        
        # Only after ALL prerequisites are added to 'output', can we add this one.
        output.append(crs)
        return True

    # We iterate over all courses because the graph might have disconnected components
    for c in range(numCourses):
        if dfs(c) == False:
            return [] # If ANY course leads to a cycle, it's impossible to graduate.
            
    return output

if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]
    print(f"Input: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"Output: {findOrder(numCourses, prerequisites)}")
