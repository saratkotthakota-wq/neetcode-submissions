class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curmin = 1
        curmax = 1
        maxProd = nums[0]
        for num in nums:
            temp = curmax * num
            curmax = max(num, temp, curmin * num)
            curmin = min(num, temp, curmin * num)
            maxProd = max(maxProd, curmax)
        return maxProd