class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific = set()
        atlantic = set()

        def dfs(row, col, ocean, prev):
            if row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0]):
                return
            if heights[row][col] >= prev:
                if (row, col) not in ocean:
                    ocean.add((row, col))
                    dfs(row-1, col, ocean, heights[row][col])
                    dfs(row+1, col, ocean, heights[row][col])
                    dfs(row, col-1, ocean, heights[row][col])
                    dfs(row, col+1, ocean, heights[row][col])

        for col in range(0, len(heights[0])):
            row = 0
            dfs(row, col, pacific, 0)
        
        for row in range(0, len(heights)):
            col = 0
            dfs(row, col, pacific, 0)

        for col in range(0, len(heights[0])):
            row = len(heights)-1
            dfs(row, col, atlantic, 0)
        
        for row in range(0, len(heights)):
            col = len(heights[0])-1
            dfs(row, col, atlantic, 0)
        
        out = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in atlantic and (row, col) in pacific:
                    out.append([row, col])
        return out



        

        