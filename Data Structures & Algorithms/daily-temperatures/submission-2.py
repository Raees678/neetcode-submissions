# [(1, 38), (2, 30)]
# (3, 36)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_i, _ = stack.pop()
                res[prev_i] = i - prev_i
            stack.append((i, temp))
        
        return res
        
