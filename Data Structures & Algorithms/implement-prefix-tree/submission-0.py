class PrefixTree:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        curr = self.trie
        for l in word:
            if l in curr:
                curr = curr[l]
            else:
                curr[l] = {}
                curr = curr[l]
        curr["*"] = 1


    def search(self, word: str) -> bool:
        if not word:
            return True
        
        i = 0
        curr = self.trie
        while i < len(word):
            if word[i] not in curr:
                return False
            else:
                curr = curr[word[i]]
            i += 1
        return "*" in curr
        

    def startsWith(self, word: str) -> bool:
        if not word:
            return True
        
        i = 0
        curr = self.trie
        while i < len(word):
            if word[i] not in curr:
                return False
            else:
                curr = curr[word[i]]
            i += 1
        return True