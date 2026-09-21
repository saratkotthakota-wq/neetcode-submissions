class Solution {
    /**
     * @param {number[]} coins
     * @param {number} amount
     * @return {number}
     */
    coinChange(coins: number[], amount: number): number {
        let mp = new Map<number, number>();

        const dfs = (amount) => {
            if (amount === 0) return 0;
            if (mp.has(amount)) return mp.get(amount);
            let minVal = 10000000000000000000;
            for (const c of coins) {
                if (amount - c >= 0) {
                    minVal = Math.min(minVal, 1+dfs(amount-c));
                }
            }
            mp.set(amount, minVal)
            return minVal
        }
        let val = dfs(amount);
        if (val === 10000000000000000000) {
            return -1;
        }
        return val;
    }
}
