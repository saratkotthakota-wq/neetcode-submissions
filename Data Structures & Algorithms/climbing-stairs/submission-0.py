class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1]*n

        def recurse(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if cache[i] != -1:
                return cache[i]
            else:
                val = recurse(i+1) + recurse(i+2)
                cache[i] = val
                return val
        return recurse(0)
        