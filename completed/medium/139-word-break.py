class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # start with true to allow us to check first word
        dp = [True] + [False] * len(s)

        # iterate over the word string
        for i in range(1, len(s) + 1):
            # iterate over the word dictionary
            for w in wordDict:
                start = i - len(w)

                # check if the word is in the dictionary and if the start index is true
                if start >= 0 and dp[start] and s[start: i] == w:
                    dp[i] = True
                    break

        return dp[-1]