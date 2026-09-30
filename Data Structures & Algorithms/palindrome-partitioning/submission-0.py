class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []

        def backtrack(i, j, curr):
            if i == len(s):
                out.append(curr[:])
                return
            if j == len(s):
                return
            if self.isPali(s, i, j):
                curr.append(s[i: j+1])
                backtrack(j+1, j+1, curr)
                curr.pop()
            backtrack(i, j+1, curr)
        backtrack(0, 0, [])
        return out
            
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True