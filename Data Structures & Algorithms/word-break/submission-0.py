class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        hashmap = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in hashmap:
                return hashmap[i]
            for word in wordDict:
                if s.startswith(word, i):
                    if dfs(i+len(word)):
                        hashmap[i] = True
                        return hashmap[i]
            hashmap[i] = False
            return  hashmap[i]
        return dfs(0)