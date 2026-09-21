class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices: number[]): number {
        let prof = 0;
        let minBuy = prices[0];
        for (const sell of prices) {
            prof = Math.max(prof, sell-minBuy);
            minBuy = Math.min(minBuy, sell);
        }
        return prof;
    }
}
