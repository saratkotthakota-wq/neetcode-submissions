class Solution:
    def numDecodings(self, s: str) -> int:

        count = 0
        n = len(s)
        cache = [-1]*n

        def dfs(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if cache[i] != -1:
                return cache[i]
            res = dfs(i+1)
            if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            cache[i]=res
            return res

        return dfs(0)

            
        