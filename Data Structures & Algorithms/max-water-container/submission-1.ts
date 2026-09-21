class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights: number[]): number {
        let p1 = 0;
        let p2 = heights.length-1;
        let maxArea = 0;

        while (p1 < p2) {
            let area = (p2-p1)*Math.min(heights[p1], heights[p2]);
            maxArea = Math.max(maxArea, area);
            if (heights[p1] < heights[p2]) p1 += 1;
            else p2 -= 1;
        }
        return maxArea;
    }
}
