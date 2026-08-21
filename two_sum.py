class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        viewed = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in viewed:
                return [viewed[diff], i]

            viewed[num] = i
