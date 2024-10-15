class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        while l < len(s) // 2:
            r = len(s) - 1 - l
            temp = s[l]
            s[l] = s[r]
            s[r] = temp

            l += 1
    