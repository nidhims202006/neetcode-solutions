from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each number
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Create buckets where index = frequency
        # max possible frequency of any element is len(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        # Iterate backwards from highest frequency to lowest
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
