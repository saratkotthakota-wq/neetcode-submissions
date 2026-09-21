class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        
        adj = {i: [] for i in range(numCourses)}
        for req in prerequisites:
            adj[req[1]].append(req[0])
        
        arr = [0] * numCourses

        def dfs(course):
            if arr[course] == 1:
                return False
            if arr[course] == 2:
                return True
            arr[course] = 1
            for neigh in adj[course]:
                if not dfs(neigh):
                    return False
            arr[course] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True        

            
        