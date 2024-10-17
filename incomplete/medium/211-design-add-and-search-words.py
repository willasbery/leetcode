class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        current = self.root

        for letter in word:
            if letter not in current:
                current[letter] = WordDictionary()
            current = current[letter]
        current["*"] = ""

    def search(self, word: str) -> bool:
        """ Does not support the . wildcard"""
        current = self.root 

        for i in range(len(word)):
            char = word[i]

            if char == ".":
                for char1 in current.root:
                    if char1 != None and char1.search(word[i + 1:]): return True
                return False

            if char not in current.root:
                return False
            
            current = current[letter]
        
        return not current and "*" in current.root


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)