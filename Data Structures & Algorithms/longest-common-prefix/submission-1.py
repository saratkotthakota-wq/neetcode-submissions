class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for l in word:
            node.children[l] = TrieNode()
            node = node.children[l]
    def lcp(self, word: str, prelen: int) -> int:
        node = self.root
        for i in range(min(len(word), prelen)):
            if word[i] not in node.children:
                return min(i, prelen)
            node = node.children[word[i]]
        return min(len(word), prelen)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        mini = 0
        for i in range(1, len(strs)):
            if len(strs[mini]) > len(strs[i]):
                mini = i
        trie = Trie()
        trie.insert(strs[mini])
        prelen = len(strs[mini])
        for i in range(len(strs)):
            prelen = trie.lcp(strs[i], prelen)
        return strs[0][:prelen]
        