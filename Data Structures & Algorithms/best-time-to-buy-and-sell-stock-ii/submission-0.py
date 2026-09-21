class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy, sell = 0, 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit += prices[sell]-prices[buy]
                print("buy: "+str(buy)+" sell: "+str(sell)+" profit: "+str(profit))
                buy = sell
            else:
                buy = sell
            sell += 1
        return profit
        