class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        minbuy = prices[0]

        for sell in prices:
            prof = max(prof, sell-minbuy)
            minbuy = min(minbuy, sell)
        return prof
        