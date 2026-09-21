class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                top = stack.pop()
                output[top[1]] = i - top[1]
            stack.append((temperatures[i], i))
        return output

        