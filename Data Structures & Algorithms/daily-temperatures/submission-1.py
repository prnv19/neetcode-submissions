class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #idx, temp

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                idx, temp = stack.pop()
                res[idx] = i - idx
            stack.append((i, t))
        return res

        