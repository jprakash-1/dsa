"""
Problem: Time Based Key-Value Store
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Example 1:
Input: 
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output: 
[null, null, "bar", "bar", null, "bar2", "bar2"]
"""

class TimeMap:
    def __init__(self):
        # We will use a Hash Map. 
        # The key is the string 'key', and the value is a list of [value, timestamp] pairs.
        self.keyStore = {}  

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If we haven't seen this key before, initialize an empty list for it.
        if key not in self.keyStore:
            self.keyStore[key] = []
        # Append the new value and its timestamp.
        # Since timestamps are strictly increasing, this list will NATURALLY be sorted by timestamp!
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist, return an empty string safely.
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        
        # We use Binary Search to efficiently find the CLOSEST timestamp that is <= the requested timestamp.
        while l <= r:
            m = (l + r) // 2
            # If the timestamp at mid is perfectly valid (<= target timestamp)...
            if values[m][1] <= timestamp:
                # We smartly save this value! It might be the final answer, 
                # but we'll elegantly still check further right to see if there is an even CLOSER timestamp.
                res = values[m][0]
                l = m + 1
            # Otherwise, the timestamp is too far in the future, so we logically MUST search the left half.
            else:
                r = m - 1
                
        return res

if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    print(f'get("foo", 1): {obj.get("foo", 1)}')
    print(f'get("foo", 3): {obj.get("foo", 3)}')
    obj.set("foo", "bar2", 4)
    print(f'get("foo", 4): {obj.get("foo", 4)}')
    print(f'get("foo", 5): {obj.get("foo", 5)}')
