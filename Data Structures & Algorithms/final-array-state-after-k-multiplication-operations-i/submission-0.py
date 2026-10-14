class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        def operation(arr):
            mdex,mval = -1, 1e9
            for i in range(len(arr)):
                if arr[i] < mval:
                    mdex = i
                    mval = arr[i]
            arr[mdex] *= multiplier
        
        arr = nums[:]
        while k > 0:
            operation(arr)
            k -= 1
        return arr
        