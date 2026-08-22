from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            # Create a character count array of size 26 for lowercase 'a' through 'z'
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Convert the count list to a tuple so it can be used as a hashmap key
            res[tuple(count)].append(s)
            
        return list(res.values())
