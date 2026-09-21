class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        count = 0

        visit = set()

        def dfs(curr):
            visit.add(curr)
            for nei in adj[curr]:
                if nei not in visit:
                    dfs(nei)
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)
        return count
        