class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        outputmax = 0
        for num in numset:
            if num-1 in numset:
                continue
            else:
                currmax = 1
                curr = num+1
                while curr in numset:
                    currmax += 1
                    curr += 1
                if currmax >= outputmax:
                    outputmax = currmax
        return outputmax




        