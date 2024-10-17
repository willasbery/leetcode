class Trie:

    def __init__(self):
        self.root = {} # initialise hashmap

    def insert(self, word: str) -> None:
        current = self.root

        for letter in word:
            # add the letter into the hashmap
            if letter not in current:
                current[letter] = {}

            # move to the next letter in the word
            current = current[letter]

        # end of word added
        current["*"] = ""

    def search(self, word: str) -> bool:
        current = self.root

        for letter in word:
            if letter not in current:
                # if we can't find the letter in the tree, return false
                return False

            current = current[letter]

        # if we are at the end of the word, return true
        return "*" in current

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for letter in prefix:
            if letter not in current:
                # if we can't find the letter in the tree, return false
                return False

            current = current[letter]

        # if we have managed to get to this point we know it is in the tree
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)