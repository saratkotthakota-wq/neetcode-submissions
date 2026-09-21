class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 0:
            return 0
        arr1 = nums[0:n-1]
        arr2 = nums[1:n]

        c1 = [-1] * (n-1)
        c2 = [-1] * (n-1)

        def recurse(i, arrlen, cache, arr):
            if i >= arrlen:
                return 0
            
            if cache[i] != -1:
                return cache[i]

            val = max(arr[i] + recurse(i+2, arrlen, cache, arr), recurse(i+1, arrlen, cache, arr))
            cache[i] = val
            return val
        return max(recurse(0, n-1, c1, arr1), recurse(0, n-1, c2, arr2))
        