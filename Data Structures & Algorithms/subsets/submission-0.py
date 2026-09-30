class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        def backtrack(curr, start):
            out.append(curr)
            for i in range(start, len(nums)):
                backtrack(curr + [nums[i]], i + 1)

        backtrack([], 0)
        return out