"""
Problem: Hand of Straights
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
"""
import collections
import heapq

def isNStraightHand(hand, groupSize):
    # If the total number of cards isn't perfectly divisible by the group size,
    # we can't possibly form valid groups!
    if len(hand) % groupSize:
        return False
        
    # Count the 'frequency' of every distinct card in our hand.
    count = collections.Counter(hand)
    
    # We need to build straights starting from the lowest available card.
    # We dump all unique card values into a Min-Heap so we can always cleanly grab the smallest one.
    minH = list(count.keys())
    heapq.heapify(minH)
    
    # While there are still unique cards left to process...
    while minH:
        # 'first' represents the start of the straight we are currently trying to build.
        first = minH[0]
        
        # A valid straight must contain 'groupSize' consecutive numbers.
        for i in range(first, first + groupSize):
            # If the next consecutive number isn't in our hand (or we ran out), we failed!
            if i not in count:
                return False
                
            # We used one instance of this card. Decrease its frequency.
            count[i] -= 1
            
            # If we've completely used up all copies of this specific card value...
            if count[i] == 0:
                # IMPORTANT: If the card we just ran out of ISN'T the smallest card in our heap,
                # it means there's a gap! We won't be able to finish a future straight.
                if i != minH[0]:
                    return False
                # If it IS the smallest, we safely remove it from the heap.
                heapq.heappop(minH)
                
    # If we processed all cards without failing, Alice can form the groups!
    return True

if __name__ == "__main__":
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    print(f"Input: hand = {hand}, groupSize = {groupSize}")
    print(f"Output: {isNStraightHand(hand, groupSize)}")
