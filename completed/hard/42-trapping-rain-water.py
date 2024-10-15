class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res = 0

        while left < right:
            if leftMax < rightMax:
                # increment pointer
                left += 1
                # left max is the biggest of the two values, with the new left height col
                leftMax = max(leftMax, height[left])
                # leftMax - height[left] because we want to get the difference in the 
                # space, giving us the water squares
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]

        return res
            