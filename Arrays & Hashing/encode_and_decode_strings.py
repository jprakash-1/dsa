"""
Problem: Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Example 1:
Input: dummy_input = ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
"""

class Codec:
    def encode(self, strs):
        # We will build a single continuous string containing all our individual strings.
        res = ""
        for s in strs:
            # Reasoning: If we just merge strings together (e.g., "lintcode"), we won't know where one ends 
            # and the next begins. If we use a simple delimiter like ",", what if the string itself contains a ","?
            # To fix this, we prepend the length of the string followed by a special character (like "#").
            # Example: "lint" becomes "4#lint". This absolutely guarantees we know exactly how many characters to read.
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        # 'res' will hold our final decoded array of strings.
        # 'i' is our global pointer keeping track of where we are in the encoded massive string 's'.
        res, i = [], 0
        
        while i < len(s):
            # We use 'j' to look ahead and find where the delimiter "#" is located.
            j = i
            while s[j] != "#":
                j += 1
                
            # Now 'j' points exactly at the "#" character.
            # The characters between 'i' and 'j' represent the integer length of the upcoming word!
            length = int(s[i:j])
            
            # Now we know the word starts specifically at 'j + 1', and it's exactly 'length' characters long.
            # We use string slicing in python string[start : end] to extract just the word.
            res.append(s[j + 1 : j + 1 + length])
            
            # Finally, we advance our global pointer 'i' so the next loop starts at the next encoded word.
            i = j + 1 + length
            
        return res

if __name__ == "__main__":
    codec = Codec()
    dummy_input = ["lint", "code", "love", "you"]
    print(f"Input: {dummy_input}")
    encoded = codec.encode(dummy_input)
    print(f"Encoded String: {encoded}")
    decoded = codec.decode(encoded)
    print(f"Output: {decoded}")
