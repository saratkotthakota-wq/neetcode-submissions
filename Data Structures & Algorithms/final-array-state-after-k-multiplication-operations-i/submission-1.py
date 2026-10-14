class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr = nums[:]
        minhp = [[num, i] for i, num in enumerate(nums)]
        heapq.heapify(minhp)
        while k > 0:
            popped = heapq.heappop(minhp)
            num, i = popped[0], popped[1]
            arr[i] *= multiplier
            heapq.heappush(minhp, [arr[i], i])
            k -= 1
        return arr
        