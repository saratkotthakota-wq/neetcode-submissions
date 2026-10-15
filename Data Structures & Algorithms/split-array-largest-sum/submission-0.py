class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            sub = 1
            curr = 0
            for num in nums:
                curr += num
                if curr > largest:
                    sub += 1
                    curr = num
            return sub <= k
        
        l, r = max(nums), sum(nums)
        res = r
        while l<=r:
            mid = (l+r)//2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

        