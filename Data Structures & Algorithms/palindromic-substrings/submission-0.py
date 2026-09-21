class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def expand(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count
        
        for i in range(len(s)):
            even = expand(i, i+1)
            odd = expand(i, i)
            
            res += even+odd

        return res
        