"""
Problem: Gas Station
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
"""

def canCompleteCircuit(gas, cost):
    # If the absolute total gas available is less than the total gas needed 
    # to make the trip, it's mathematically impossible to complete the circuit.
    if sum(gas) < sum(cost):
        return -1
        
    # 'total' tracks our current tank level as we simulate the journey.
    # 'res' will store the index of our potential starting station.
    total = 0
    res = 0
    
    # We iterate through each station...
    for i in range(len(gas)):
        # Calculate the net change in gas if we travel from this station to the next.
        total += (gas[i] - cost[i])
        
        # If our tank ever dips below zero...
        if total < 0:
            # Traveling from our current 'res' starting point through station 'i' failed.
            # IN FACT, any starting point between our old 'res' and 'i' will also fail!
            # So, we reset our tank to 0 and try starting fresh at the *next* station (i + 1).
            total = 0
            res = i + 1
            
    # Because of our mathematical check at the very beginning, we are GUARANTEED 
    # that a solution exists. The 'res' variable currently holds the only possible answer!
    return res

if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(f"Input: gas = {gas}, cost = {cost}")
    print(f"Output: {canCompleteCircuit(gas, cost)}")
