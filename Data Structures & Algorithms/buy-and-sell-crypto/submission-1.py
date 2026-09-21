class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            diff = prices[sell] - prices[buy]
            if diff < 0:
                buy = sell
                sell = sell + 1
            elif diff > profit:
                profit = diff
            else:
                sell += 1
        return profit
        