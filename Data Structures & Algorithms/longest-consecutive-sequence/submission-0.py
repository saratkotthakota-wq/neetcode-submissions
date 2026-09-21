class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()
        for num in nums:
            numset.add(num)
        outputmax = []
        for num in numset:
            if num-1 in numset:
                continue
            else:
                currmax = [num]
                curramt = 1
                curr = num+1
                while curr in numset:
                    currmax.append(num+1)
                    curr += 1
                if len(currmax) >= len(outputmax):
                    outputmax = currmax
        return len(outputmax)




        