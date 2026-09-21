class Solution:
    def validPalindrome(self, s: str) -> bool:

        def ispalin(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return ispalin(l, r-1) or ispalin(l+1, r)
            l += 1
            r -= 1
        return True

        