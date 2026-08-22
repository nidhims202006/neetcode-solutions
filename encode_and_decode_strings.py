from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Prefix each string with its length followed by a delimiter '#'
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            # Find the delimiter '#' to parse the length of the next string
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            # Read 'length' characters after '#'
            res.append(s[j + 1 : j + 1 + length])
            # Move index past the current string to the start of the next length prefix
            i = j + 1 + length
            
        return res
