class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def backtrack(row, col, word):
            if not word:
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False 
            if word[0] != board[row][col]:
                return False
            if (row, col) in visited:
                return False
            else:
                visited.add((row, col))
                total = [backtrack(row-1, col, word[1:]), 
                    backtrack(row+1, col, word[1:]),
                    backtrack(row, col-1, word[1:]), 
                    backtrack(row, col+1, word[1:])]
                visited.remove((row, col))
                return any(total)


        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, word):
                    return True
        return False

        