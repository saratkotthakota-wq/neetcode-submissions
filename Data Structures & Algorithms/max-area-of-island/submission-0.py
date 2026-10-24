class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def dfs(row, col):
            nonlocal area
            visited[row][col] = True
            area += 1
            neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for nei in neighbors:
                r, c = row + nei[0], col + nei[1]
                if (0 <= r <= len(grid)-1) and (0 <= c <= len(grid[0])-1) and grid[r][c] == 1 and not visited[r][c]:
                    dfs(r, c)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and not visited[row][col]:
                    area = 0
                    dfs(row, col)
                    if area >= maxarea:
                        maxarea = area
        return maxarea