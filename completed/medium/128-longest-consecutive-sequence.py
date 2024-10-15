class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to set to remove duplicates
        num_set = set(nums)
        longest = 
        
        # iterate over each number in the set (which we know is unique)
        for num in num_set:
            # num - 1 not in num_set means that we are not in a consecutive sequence,
            # because if we were, num - 1 would be in the set
            if (num - 1) not in num_set:
                # new set
                length = 1
                # whilst the next consecutive number is in the set, add one 
                while (num + length) in num_set:
                    length += 1

                # update the longest variable if the current length of the concurrent set is 
                # longer than the previous example
                longest = max(length, longest)

        return longest