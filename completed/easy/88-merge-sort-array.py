class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == m:
            return nums1

        j = 0
        for num in nums2:
            while j <= len(nums1) - 1:
                if nums1[j] >= num or nums1[j] == 0:
                    temp = nums1[j: -1]
                    nums1[j] = num
                    nums1[j + 1:] = temp
                    break
                else:
                    j += 1
            
        return nums1.sort()
    
# O((m * n) + log(m + n)) time complexity, O(1) space complexity

# OTHER SOLUTIONS
    
# TWO POINTER SOLUTION
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1 # pointer for nums1
        j = n - 1 # pointer for nums2
        k = m + n - 1 # length of the merged array
        
        while j >= 0: # while there are elements in nums2
            if i >= 0 and nums1[i] > nums2[j]: # if there are elements in nums1 and the element in nums1 is greater than the element in nums2
                nums1[k] = nums1[i] # set the element in nums1 to the end of the merged array
                i -= 1 # decrement the pointer for nums1
            else:
                nums1[k] = nums2[j] # set the element in nums2 to the end of the merged array
                j -= 1 # decrement the pointer for nums2
            k -= 1 # decrement the length of the merged array