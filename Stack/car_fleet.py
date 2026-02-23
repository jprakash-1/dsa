"""
Problem: Car Fleet
There are n cars going to the same destination along a one-lane road. The destination is target miles away.
Return the number of car fleets that will arrive at the destination.

Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
"""

def carFleet(target, position, speed):
    # Group each car's starting position and speed together.
    pair = [[p, s] for p, s in zip(position, speed)]
    
    # We will use a Stack to mathematically keep track of the arrival times of unique car fleets.
    stack = []
    
    # We MUST process cars starting from the closest to the target (Reverse Sorted Order).
    # Why? Because a car behind can only catch up to a car ahead of it, never the other way around!
    for p, s in sorted(pair)[::-1]:
        # Calculate exactly how long this specific car takes to reach the target: (Distance / Speed)
        stack.append((target - p) / s)
        
        # Collision Check:
        # If we have at least 2 cars tracked, and the car we just added (behind) arrives 
        # FASTER or at the EXACT SAME TIME (<=) as the car ahead of it...
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            # It means they literally crashed into each other and formed a single fleet!
            # So we remove the faster car's time, because the fleet is bottlenecked by the slower car ahead.
            stack.pop()
            
    # The number of unique arrival times left in our stack is precisely the number of fleets!
    return len(stack)

if __name__ == "__main__":
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(f"Input: target = {target}, position = {position}, speed = {speed}")
    print(f"Output: {carFleet(target, position, speed)}")
