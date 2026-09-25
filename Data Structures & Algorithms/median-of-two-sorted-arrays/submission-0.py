class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        smaller, larger = [], []
        if len(nums1) <= len(nums2):
            smaller = nums1
            larger = nums2
        else:
            smaller = nums2
            larger = nums1
        
        total = len(smaller) + len(larger)
        half = total//2
        
        l, r = 0, len(smaller)-1
        while True:
            small = (l+r)//2
            large = half - small - 2
            Aleft = smaller[small] if small >= 0 else float("-infinity")
            Aright = smaller[small + 1] if (small + 1) < len(smaller) else float("infinity")
            Bleft = larger[large] if large >= 0 else float("-infinity")
            Bright = larger[large + 1] if (large + 1) < len(larger) else float("infinity")
            if Aleft <= Bright and Bleft<=Aright:
                if total%2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft)+min(Aright, Bright))/2 
            elif Aleft > Bright:
                r = small - 1
            elif Bleft > Aright:
                l = small + 1

        