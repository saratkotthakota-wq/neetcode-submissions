class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append([row, col])
                    visited.add((row, col))
        def addcell(row, col):
            if (0 <= row <= len(grid)-1) and (0 <= col <= len(grid[0])-1) and ((row, col) not in visited) and (grid[row][col] != -1):
                visited.add((row, col))
                queue.append([row, col])
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for nei in neighbors:
                    addcell(r+nei[0], c+nei[1])
            dist += 1



        