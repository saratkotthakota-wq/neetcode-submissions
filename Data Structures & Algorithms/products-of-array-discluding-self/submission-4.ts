class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        let out = Array(nums.length).fill(1)

        let prefix = 1;
        for (let i = 0; i < nums.length; i++) {
            out[i] *= prefix;
            prefix *= nums[i];
        }
        let suffix = 1;
        for (let i = nums.length-1; i >= 0; i--){
            out[i] *= suffix;
            suffix *= nums[i];
        }
        return out
    }
}
