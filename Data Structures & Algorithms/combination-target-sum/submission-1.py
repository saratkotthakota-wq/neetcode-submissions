class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        out = []
        nums = sorted(nums)

        def dfs(i, curr, target):
            if target == 0:
                out.append(curr[:])
                return
            for j in range(i, len(nums)):
                if target - nums[j] < 0:
                    break
                curr.append(nums[j])
                dfs(j, curr, target-nums[j])
                curr.remove(nums[j])
        dfs(0, [], target)
        return out
        