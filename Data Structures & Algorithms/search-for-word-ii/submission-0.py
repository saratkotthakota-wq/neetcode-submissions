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


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        for word in words:
            trie.insert(word)

        def getNeighbors(row, col):
            out = []
            if row > 0:
                out.append([row - 1, col])
            if row < len(board) - 1:
                out.append([row + 1, col])
            if col > 0:
                out.append([row, col - 1])
            if col < len(board[0]) - 1:
                out.append([row, col + 1])
            return out

        res = set()
        visit = set()

        def dfs(row, col, curr, word):
            if (row, col) in visit or board[row][col] not in curr:
                return
            visit.add((row, col))
            curr = curr[board[row][col]]
            word += board[row][col]
            if "*" in curr:
                res.add(word)

            neighbors = getNeighbors(row, col)
            for neigh in neighbors:
                dfs(neigh[0], neigh[1], curr, word)
            visit.remove((row, col))
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, trie.trie, "")
        return list(res)