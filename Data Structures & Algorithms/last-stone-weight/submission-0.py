class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            st1 = -1*heapq.heappop(stones)
            st2 = -1*heapq.heappop(stones)
            if st1 > st2:
                heapq.heappush(stones, -1*(st1-st2))
            elif st2 > st1:
                heapq.heappush(stones, -1*(st2-st1))
        return -1*heapq.heappop(stones) if stones else 0