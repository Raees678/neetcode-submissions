# this is different from trapping rain water since  we care 
# about the heights of ALL intermediate rectangles not just the edges
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Find the next smaller element index for a bar
        # Find the previous smaller element index for a bar

        next_smaller_index = [len(heights)] * len(heights)
        prev_smaller_index = [-1] * len(heights)
        
        stack = [] # increasing
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                popped_i = stack.pop()
                next_smaller_index[popped_i] = i
            stack.append(i)
        
        stack = []
        for i in reversed(range(len(heights))):
            while stack and heights[stack[-1]] > heights[i]:
                popped_i = stack.pop()
                prev_smaller_index[popped_i] = i
            stack.append(i)
        
        max_area = 0
        for i in range(len(heights)):
            width = next_smaller_index[i] - prev_smaller_index[i] - 1
            height = heights[i]
            area = width * height
            max_area = max(area, max_area)
        
        return max_area






        

        

        
        
        

