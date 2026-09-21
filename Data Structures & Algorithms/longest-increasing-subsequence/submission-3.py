class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        hashmap = {}

        maxlen = 0
        def recurse(i, j):
            if i >= len(nums):
                return 0
            if (i, j) in hashmap:
                return hashmap[(i, j)]
            count = 0
            if j == -1 or nums[i]>nums[j]:
                count = max(1+recurse(i+1, i), recurse(i+1, j))
            else:
                count = recurse(i+1, j)
            hashmap[(i, j)] = count
            return count

        maxlen = recurse(0, -1)
        return maxlen


        