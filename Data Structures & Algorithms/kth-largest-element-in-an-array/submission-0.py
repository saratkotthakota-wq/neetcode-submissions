class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minhp = []
        for num in nums:
            heapq.heappush(minhp, num)
            if len(minhp) > k:
                heapq.heappop(minhp)
        return heapq.heappop(minhp)
        