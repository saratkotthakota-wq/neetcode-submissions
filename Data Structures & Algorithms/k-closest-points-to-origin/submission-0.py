class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            total = x**2+y**2
            return -1*math.sqrt(total)
        maxhp = []
        for x, y in points:
            heapq.heappush(maxhp, (dist(x,y), x, y))
            if len(maxhp) > k:
                heapq.heappop(maxhp)
        out = [[p[1], p[2]] for p in maxhp]
        return out