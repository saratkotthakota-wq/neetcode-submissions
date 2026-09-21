class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        curr = self.trie
        for l in word:
            if l in curr:
                curr = curr[l]
            else:
                curr[l] = {}
                curr = curr[l]
        curr["*"] = 1
        

    def search(self, word: str) -> bool:

        def dfs(left, root):

            curr = root

            for i in range(left, len(word)):
                l = word[i]
                if l == ".":
                    return any(dfs(i + 1, child) for child in curr.values() if isinstance(child, dict))
                else:
                    if l not in curr:
                        return False
                    curr = curr[l]
            return "*" in curr

        return dfs(0, self.trie)
