class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        start = image[sr][sc]
        if start == color:
            return image
        queue = deque([[sr, sc]])
        while queue:
            popped = queue.popleft()
            image[popped[0]][popped[1]] = color
            neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for nei in neighbors:
                if (0 <= popped[0]+nei[0] <= len(image)-1) and (0 <= popped[1]+nei[1] <= len(image[0])-1) and image[popped[0]+nei[0]][popped[1]+nei[1]] == start:
                    queue.append([popped[0]+nei[0], popped[1]+nei[1]])
        return image
        