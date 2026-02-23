"""
Problem: Partition Labels
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
"""

def partitionLabels(s):
    # Step 1: Find the LAST occurrence of each character in the string.
    # Why? Because if we include a character in a partition, that partition MUST 
    # stretch at least as far as its last occurrence to keep all identical characters together!
    lastIndex = {}  # char -> last index in s
    for i, c in enumerate(s):
        lastIndex[c] = i
        
    res = []
    size, end = 0, 0
    
    # Step 2: Iterate through the string to build our partitions.
    for i, c in enumerate(s):
        size += 1 # We add the current character to our running partition size
        
        # We continually update the 'end' goalpost of our current partition.
        # It must be the maximum last occurrence of ALL characters we've seen so far in this chunk.
        end = max(end, lastIndex[c])
        
        # If our current index finally reaches the required 'end' goalpost...
        if i == end:
            # We've successfully completed a valid partition!
            res.append(size) # Save its size
            size = 0         # Reset the size counter for the next partition
            
    return res

if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    print(f"Input: s = '{s}'")
    print(f"Output: {partitionLabels(s)}")
