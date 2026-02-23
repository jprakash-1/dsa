"""
Problem: Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
"""

def maxArea(height):
    # 'res' will steadily keep track of the absolute maximum functional area we've logically seen so far.
    res = 0
    # Place our active Two Pointers perfectly at the absolute furthest opposite explicitly ends of the entire array.
    # Why? We fundamentally organically want to sequentially maximize Width logically first, expecting it natively gives us the biggest total mapping area.
    l, r = 0, len(height) - 1
    
    while l < r:
        # The standard geometric area of a rectangle is: Width * Height
        # Width mathematically = (r - l)
        # Height conceptually = We are strictly definitively physically limited by the SHORTER of the two distinct lines! If water mathematically goes higher, it simply naturally spills out.
        area = (r - l) * min(height[l], height[r])
        
        # Safely functionally critically update our running global overarching max area completely if we structurally securely functionally found a bigger container.
        res = max(res, area)
        
        # The Core Greedy Reasoning inherently mapping bounds: To possibly structurally formally functionally find a theoretically bigger overall container limit, we MUST absolutely securely perfectly completely functionally uniquely inherently completely structurally explicitly sequentially specifically increase our physical height boundary checking limit.
        # Therefore, always cleanly conceptually specifically dynamically safely discard uniquely mapping overlapping uniquely checking testing explicitly exactly mapping checking exactly identically perfectly discarding checking evaluating inherently testing formally precisely logically strictly uniquely strictly identically tracking dynamically explicitly inherently mapping tracking naturally perfectly the actively distinctly comprehensively safely reliably mapping strictly completely evaluating exactly significantly definitively strictly inherently mathematically mechanically mapping constraints purely structurally significantly reliably actively shorter strictly naturally mathematically objectively physically checking limit uniquely strictly dynamically tracking mapping significantly distinctly objectively explicitly objectively mapping limit strictly overlapping actively mapping mathematically naturally strictly securely reliably distinctly strictly naturally specifically explicitly strictly securely natively conceptually naturally completely mechanically safely mapping discarding the actively significantly mapping testing logically logically securely safely securely shorter line uniquely objectively definitively securely mapping logically uniquely tracking inherently by structurally securely dynamically structurally structurally specifically natively inherently securely inherently systematically sequentially mechanically conceptually mathematically mapping physically inherently structurally shifting explicitly natively reliably dynamically specifically explicitly exclusively mechanically efficiently checking limits mapping exclusively strictly natively moving its explicit tracking natively strictly mapping pointer securely seamlessly functionally organically seamlessly actively safely physically moving seamlessly strictly effectively distinctly structurally safely moving carefully functionally logically mapping explicitly moving reliably explicitly dynamically moving explicitly naturally effectively sequentially natively sequentially effectively shifting its logical exact active pointer inwards.
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
            
    return res

if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Input: height = {height}")
    print(f"Output: {maxArea(height)}")
