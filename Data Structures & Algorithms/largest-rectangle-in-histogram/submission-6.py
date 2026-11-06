class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        next_smallest = [len(heights)] * len(heights)
        prev_smallest = [-1] * len(heights)
        
        for i, h in enumerate(heights):
            while stack and h < stack[-1][1]:
                prev_i, prev_h = stack.pop()
                next_smallest[prev_i] = i
            
            if stack:
                prev_smallest[i] = stack[-1][0]
            stack.append((i, h))
        
        res = 0
        for i in range(len(heights)):
            l = prev_smallest[i] + 1
            r = next_smallest[i] - 1
            width = r - l + 1
            height = heights[i]
            area = width * height
            res = max(res, area)
        
        return res
        

        
