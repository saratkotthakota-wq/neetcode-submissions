class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        adj[-1] = [0]

        visit = set()
        
        def dfs(curr, parent):
            if curr in visit:
                return False
            visit.add(curr)
            for nei in adj[curr]:
                if nei != parent:
                    if not dfs(nei, curr):
                        return False
            return True

        return dfs(0, -1) and len(visit) == n

        