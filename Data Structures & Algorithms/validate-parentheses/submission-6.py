class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        starts = set(['[', '{', '('])
        ends = {
            ')': '(',
            '}': '{',
            ']': '[' 
        }
        for l in s:
            if l in starts:
                stack.append(l)
            else:
                if l not in ends or not stack or ends[l] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0           
        