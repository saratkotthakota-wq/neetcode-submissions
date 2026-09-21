class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
        nums.sort((a, b) => {
            return a-b;
        });
        const res = [];
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] === nums[i - 1]) continue;
            let target = 0 - nums[i];
            let l = i + 1;
            let r = nums.length-1;
            while (l < r) {
                if (nums[l] + nums[r] > target) {
                    r--;
                }
                else if (nums[l] + nums[r] < target) {
                    l++;
                }
                else {
                    res.push([nums[i], nums[l], nums[r]]);
                    l++;
                    r--;
                    while (l < r && nums[l] === nums[l-1]) {
                        l++
                    }
                }

            }
        }
        return res;
    }
}
