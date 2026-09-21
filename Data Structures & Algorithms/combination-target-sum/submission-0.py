class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []

        def backtrack(start, target, used):
            if target < 0:
                return
            if target == 0:
                out.append(used[:])
            else:
                for i in range(start, len(nums)):
                    used.append(nums[i])
                    backtrack(i, target-nums[i], used)
                    used.remove(nums[i])

        used = []
        backtrack(0, target, used)
        return out
        