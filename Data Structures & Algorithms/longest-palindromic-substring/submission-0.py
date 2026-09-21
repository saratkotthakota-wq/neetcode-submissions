class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res, resLen = 0, 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, s[l + 1:r]
        
        for i in range(len(s)):
            starte, even = expand(i, i+1)
            starto, odd = expand(i, i)
            
            curr = ""
            startc = -1
            if len(even) > len(odd):
                curr = even
                startc = starte
            else:
                curr = odd
                startc = starto
            if len(curr) > resLen:
                resLen = len(curr)
                res = startc

        return s[res:res+resLen]