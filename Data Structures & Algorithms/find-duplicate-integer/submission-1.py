class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow2
        