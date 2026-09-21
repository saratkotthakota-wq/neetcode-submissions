class Solution:
    def isValid(self, s: str) -> bool:
        open = {'(', '{', '['}
        close = {')', '}', ']'}
        stack = []
        for char in s:
            if char in open:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif char == ')' and stack[-1] == '(':
                    del stack[-1]
                elif char == '}' and stack[-1] == '{':
                    del stack[-1]
                elif char == ']' and stack[-1] == '[':
                    del stack[-1]
                else:
                    return False
        if len(stack) == 0:
            return True
        else: return False
        