class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        out = []

        def backtrack(openct, closect, curr):
            if openct == closect == n:
                out.append(curr)
                return
            if openct < n:
                curr += "("
                backtrack(openct+1, closect, curr)
                curr = curr[:-1]
            if closect < openct:
                curr += ")"
                backtrack(openct, closect+1, curr)
                curr = curr[:-1]

        backtrack(0, 0, "")
        return out
        