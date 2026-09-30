class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        out = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(i, curr):
            if i == len(digits):
                out.append(curr)
                return
            for l in digitToChar[digits[i]]:
                backtrack(i+1, curr+l)
        if digits:
            backtrack(0, "")
        return out