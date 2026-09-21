class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        newnums = sorted(nums)
        output = set()
        for i in range(len(newnums)-2):
            target = 0 - newnums[i]
            p1 = i+1
            p2 = len(newnums)-1
            while (p1 < p2):
                if newnums[p1]+newnums[p2] == target:
                    output.add(tuple([newnums[i], newnums[p1], newnums[p2]]))
                    p1 += 1
                    p2 -= 1
                elif newnums[p1]+newnums[p2] > target:
                    p2 -= 1
                else:
                    p1 += 1
        real = []
        for tup in output:
            real.append(list(tup))
        return real


        