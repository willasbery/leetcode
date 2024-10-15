class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matches = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for char in s:
            if char not in matches:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                prev = stack.pop()
                if matches[char] != prev:
                    return False
        
        return True if len(stack) == 0 else False

        