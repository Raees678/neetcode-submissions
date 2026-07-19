class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      d = defaultdict(int)
      stack = []
      for (i, temp) in enumerate(temperatures):
        while len(stack) > 0 and stack[-1][0] < temp:
          (old_temp, old_i) = stack.pop()
          d[old_i] = i - old_i

        stack.append((temp, i))
      
      res = [0] * len(temperatures)
      for i in d:
        res[i] = d[i]
      
      return res
      
      

        
        