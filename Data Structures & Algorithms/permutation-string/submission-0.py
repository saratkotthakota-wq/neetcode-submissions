class Solution:

    def getFreq(self, window):
        arr = [0]*26
        for l in window:
            num = ord(l)-ord('a')
            arr[num] += 1
        return arr
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        arr = self.getFreq(s1)

        l, r = 0, len(s1)-1
        window = s2[l:r+1]
        windowarr = self.getFreq(window)
        while r < len(s2):
            if windowarr == arr:
                return True
            else:
                num = ord(s2[l])-ord('a')
                windowarr[num] -= 1
                l += 1
                r += 1
                if r < len(s2):
                    num = ord(s2[r])-ord('a')
                    windowarr[num] += 1
        return False
