class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []

        def backtrack(curr, start):
            out.append(curr)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtrack(curr + [nums[i]], i + 1)
        backtrack([], 0)
        return out

        