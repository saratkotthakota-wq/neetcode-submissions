class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for i, val in enumerate(nums):
            if val != 0:
                self.pairs.append([i, val])
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        p1, p2 = 0, 0
        while p1 < len(self.pairs) and p2 < len(vec.pairs):
            if self.pairs[p1][0] == vec.pairs[p2][0]:
                res += self.pairs[p1][1] * vec.pairs[p2][1]
                p1 += 1
                p2 += 1
            elif self.pairs[p1][0] < vec.pairs[p2][0]:
                p1 += 1
            else:
                p2 += 1
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
