class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy, sell = 0, 1

        while sell < len(prices):
            profit = max(profit, prices[sell]-prices[buy])
            if prices[buy] > prices[sell]:
                buy = sell
            sell += 1
        return profit



        