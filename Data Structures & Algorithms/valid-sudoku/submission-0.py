class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def getIndex(row: int, col: int) -> int:
            return int(row/3)*3 + int(col/3)
        hashRow = [set() for _ in range(9)]
        hashCol = [set() for _ in range(9)]
        hashSquare= [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                else:
                    index = getIndex(i, j)
                    if num in hashRow[i] or num in hashCol[j] or num in hashSquare[int(index)]:
                        print("row: "+str(i)+" and col: "+str(j)+" and num: "+str(num)+" and index: "+str(int(index)))
                        print(hashRow)
                        print(hashCol[j])
                        print(hashSquare[int(index)])
                        return False
                    else:
                        hashRow[i].add(num)
                        hashCol[j].add(num)
                        hashSquare[int(index)].add(num)
        return True

        