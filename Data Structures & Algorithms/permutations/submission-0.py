class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []

        def backtrack(perm, picked):
            if len(perm) == len(nums):
                out.append(list(perm))
                return
            for i in range(len(nums)):
                if not picked[i]:
                    perm.append(nums[i])
                    picked[i] = True
                    backtrack(perm, picked)
                    perm.pop()
                    picked[i] = False
        backtrack([], [False]*len(nums))
        return out