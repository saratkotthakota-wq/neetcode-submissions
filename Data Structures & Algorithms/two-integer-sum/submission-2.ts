class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const seen = new Map<number, number>();
        for (let i = 0; i < nums.length; i++) {
            let need = target - nums[i]
            if (seen.has(need)){
                return [seen.get(need)!, i]
            }
            seen.set(nums[i], i)
        }
        return [-1, -1]
    }
}
