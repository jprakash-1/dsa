"""
Problem: Merge Triplets to Form Target Triplet
A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.
To obtain target, you may apply the following operation on triplets any number of times (possibly zero):
Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.

Example 1:
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
"""

def mergeTriplets(triplets, target):
    # 'good' will mathematically track which components of the target triplet (x, y, or z)
    # we have successfully "found" in valid triplets.
    # It stores indices (0, 1, or 2).
    good = set()
    
    for t in triplets:
        # A triplet is "toxic" if ANY of its values are strictly GREATER than the target values.
        # Why? Because merging (taking the max) with a toxic triplet would permanently ruin our chances 
        # of exactly hitting the target. We must IGNORE toxic triplets.
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue
            
        # If the triplet is "safe", we check if it perfectly matches the target at any position.
        for i, v in enumerate(t):
            if v == target[i]:
                # If it does, we record that we've found a way to achieve target[i]!
                good.add(i)
                
    # If we successfully found safe triplets that collectively contain the target x, y, AND z,
    # then our set 'good' will have exactly 3 items (indices 0, 1, and 2).
    return len(good) == 3

if __name__ == "__main__":
    triplets = [[2,5,3],[1,8,4],[1,7,5]]
    target = [2,7,5]
    print(f"Input: triplets = {triplets}, target = {target}")
    print(f"Output: {mergeTriplets(triplets, target)}")
