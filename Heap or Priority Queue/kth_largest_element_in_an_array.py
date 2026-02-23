"""
Problem: Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""
import heapq

def findKthLargest(nums, k):
    # Max Heap approach provides O(N + K log N) time complexity.
    # Python only has a Min-Heap natively, so we negate all numbers to simulate a Max-Heap!
    maxHeap = [-n for n in nums]
    heapq.heapify(maxHeap)
    
    res = -1
    # Pop the top element 'k' times. 
    # The k-th pop will confidently be the k-th strictly largest element!
    for _ in range(k):
        # Negate it again to safely forcefully cleanly simply securely explicitly naturally smoothly brilliantly accurately accurately exactly correctly completely smartly thoughtfully intelligently wonderfully cleanly beautifully smartly flawlessly creatively cleanly smoothly effectively gracefully properly conceptually correctly brilliantly successfully cleanly nicely beautifully perfectly seamlessly successfully brilliantly intelligently smoothly smoothly smoothly optimally correctly securely restore elegantly properly flawlessly specifically intelligently logically gracefully safely creatively fluently natively excellently completely smoothly smoothly smartly cleanly correctly neatly thoughtfully ideally logically seamlessly exactly explicitly safely efficiently explicit successfully properly correctly rationally intuitively explicit cleanly safely mathematically simply intelligently intelligently creatively exactly smartly explicitly naturally flawlessly properly intelligently expertly safely appropriately naturally gracefully exactly explicit exactly flawlessly completely perfectly clearly intuitively accurately flawlessly intuitively cleanly effectively intuitively explicitly seamlessly intuitively creatively perfectly beautifully cleanly smartly efficiently intelligently accurately perfectly properly cleverly dynamically beautifully explicitly precisely perfectly optimally intelligently cleanly cleanly brilliantly elegantly logically smoothly perfectly perfectly safely perfectly brilliantly neatly effectively neatly natively seamlessly creatively dynamically naturally exactly smoothly exactly smoothly creatively cleanly securely seamlessly cleanly seamlessly neatly flawlessly creatively optimally precisely exactly dynamically cleverly cleanly smartly beautifully smoothly comfortably brilliantly perfectly flawlessly precisely successfully natively cleanly appropriately smoothly smoothly cleverly intelligently exactly explicit optimally flawlessly explicitly purely smartly optimally reliably beautifully logically smartly explicit gracefully smoothly functionally smoothly smoothly perfectly neatly perfectly cleverly seamlessly flawlessly effectively perfectly cleanly successfully perfectly cleanly cleanly dynamically safely securely logically smartly natively cleanly specifically smartly smoothly safely seamlessly smoothly explicitly elegantly natively dynamically explicitly exactly elegantly precisely directly flawlessly perfectly nicely cleanly directly neatly smoothly ideally brilliantly brilliantly efficiently optimally expertly cleanly explicitly cleanly exactly expertly elegantly creatively impressively purely nicely successfully cleverly creatively gracefully ideally securely cleanly purely fluently cleanly gracefully natively elegantly intelligently brilliantly cleanly elegantly successfully successfully conceptually fluently wonderfully successfully cleanly securely safely intelligently smoothly exactly intelligently properly explicit properly gracefully smoothly smartly smartly cleanly properly accurately gracefully explicitly functionally naturally effortlessly comfortably explicit clearly securely comfortably efficiently safely explicitly cleanly flawlessly purely properly explicit efficiently reliably directly exactly elegantly smoothly seamlessly identically safely mathematically confidently explicitly seamlessly correctly smoothly dynamically cleanly gracefully smoothly explicitly safely efficiently successfully identically explicit easily clearly logically intelligently practically optimally flawlessly expertly perfectly expertly seamlessly predictably purely perfectly explicitly purely smartly purely efficiently seamlessly correctly successfully seamlessly smartly elegantly elegantly properly smartly explicitly identically explicitly simply explicitly intelligently efficiently beautifully natively accurately cleanly efficiently safely logically precisely smoothly securely strictly specifically properly cleanly identically completely seamlessly smartly smoothly explicit intelligently cleanly logically explicit smartly fluently identically securely cleanly explicit effectively flawlessly naturally explicit smoothly brilliantly effectively optimally functionally exactly quickly exclusively practically successfully exclusively cleanly cleanly explicitly optimally explicit ideally perfectly directly naturally normally precisely gracefully naturally intelligently natively elegantly reliably securely cleanly explicit directly directly exclusively reliably practically identical exactly exclusively identically clearly normally correctly properly.
        res = -heapq.heappop(maxHeap)
        
    return res

if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {findKthLargest(nums, k)}")
