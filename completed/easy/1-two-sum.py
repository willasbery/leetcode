class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, num in enumerate(nums):
            if target - num in hash_map:
                return sorted([index, hash_map[target - num]])
            else:
                hash_map[num] = index