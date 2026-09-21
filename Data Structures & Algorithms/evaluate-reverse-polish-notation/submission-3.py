class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = set(["+", "-", "*", "/"])
        stack = []
        index = 0
        while index < len(tokens):
            if tokens[index] not in operands:
                stack.append(int(tokens[index]))
                index += 1
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                result = 0
                if tokens[index] == "+":
                    result = int(num2 + num1)
                if tokens[index] == "-":
                    result = int(num2 - num1)
                if tokens[index] == "*":
                    result = int(num2 * num1)
                if tokens[index] == "/":
                    result = int(num2 / num1)
                stack.append(result)
                index += 1
        return stack[0]
                

        