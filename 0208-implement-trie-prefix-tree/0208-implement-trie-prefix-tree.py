class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEndofWord = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            char_id = ord(c) - ord("a")
            if not curr.children[char_id]:
                curr.children[char_id] = Trie()
            curr = curr.children[char_id]

        curr.isEndofWord = True


    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            char_id = ord(c) - ord("a")
            if not curr.children[char_id]:
                return False
            curr = curr.children[char_id]

        return True and curr.isEndofWord
            
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            char_id = ord(c) - ord("a")
            if not curr.children[char_id]:
                return False
            curr = curr.children[char_id]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)