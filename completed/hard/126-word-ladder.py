class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        changes = 1
        queue = deque([beginWord])
        visited = set([beginWord]) # covert to set to remove duplicates
        wordList = set(wordList) # covert to set to remove duplicates

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        while queue:
            for l in range(len(queue)):
                current_word = queue.popleft()

                if current_word == endWord:
                    return changes

                # find and replace every letter in the current word
                for i in range(len(current_word)):
                    # split the word like this:
                    # current_word = dog
                    # prefix = d, suffix = g
                    # then we can insert chars to try get new words
                    prefix, suffix = current_word[: i], current_word[i + 1:]

                    for letter in alphabet:
                        w = prefix + letter + suffix

                        # if we find a word that is in the wordlist,
                        # i.e the changes we made make a new word in the wordlist
                        if w in wordList and w not in visited:
                            queue.append(w)
                            visited.add(w)

            changes += 1

        return 0