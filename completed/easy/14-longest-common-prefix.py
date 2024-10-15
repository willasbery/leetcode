class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        shortest_chars = list(shortest)

        strs.remove(shortest)
        longest = ""

        for i, char in enumerate(shortest_chars):
            for string in strs:
                if string[i] != char:
                    return longest
            
            longest += char

        return longest
            

        