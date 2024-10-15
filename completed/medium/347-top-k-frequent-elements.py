class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1
            
        # sort the dictionary by value, in descending order
        hash_map = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in hash_map[:k]]