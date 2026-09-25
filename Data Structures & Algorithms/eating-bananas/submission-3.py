class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        mink = r
        while l <= r:
            mid = (l+r)//2
            t = 0
            for p in piles:
                t += -1*(-1*p//mid)
            if t > h:
                l = mid+1
            else:
                mink = min(mink, mid)
                r = mid-1
        return mink
