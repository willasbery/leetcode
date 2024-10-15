class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumerical = ""

        for char in s:
            if char.isnumeric() == True or char.isalpha() == True:
                alphanumerical += char.lower()

        return alphanumerical == alphanumerical[::-1]