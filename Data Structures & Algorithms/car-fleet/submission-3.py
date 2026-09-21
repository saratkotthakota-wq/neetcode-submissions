class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = list(zip(position,speed))
        sortedp = sorted(pairs, reverse=True)
        for pos, spe in sortedp:

            time = (target-pos)/spe
            if stack:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)
        return len(stack)
        


        