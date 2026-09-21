class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    count += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
        time = 0
        while queue and count > 0:
            n = len(queue)
            while n > 0:
                rotten = queue.pop(0)
                n -= 1
                neighbors = [(rotten[0]+1, rotten[1]), (rotten[0]-1, rotten[1]), (rotten[0], rotten[1]+1), (rotten[0], rotten[1]-1)]
                for nei in neighbors:
                    if nei[0] > -1 and nei[0] < len(grid) and nei[1] > -1 and nei[1] < len(grid[0]) and grid[nei[0]][nei[1]] == 1:
                        grid[nei[0]][nei[1]] = 2
                        count -= 1
                        queue.append((nei[0], nei[1]))
            time += 1
        if count == 0:
            return time
        return -1
            

        