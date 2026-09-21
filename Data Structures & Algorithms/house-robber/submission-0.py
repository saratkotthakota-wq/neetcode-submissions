class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        cache = [-1]*n

        def recurse(i, n):
            if i >= n:
                return 0
            
            if cache[i] != -1:
                return cache[i]

            val = max(nums[i] + recurse(i+2, n), recurse(i+1, n))
            cache[i] = val
            return val
        return recurse(0, n)


        