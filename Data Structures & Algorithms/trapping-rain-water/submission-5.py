class Solution:
    def trap(self, height: List[int]) -> int:
        next_largest = [0] * len(height)
        prev_largest = [0] * len(height)

        for i in range(len(height)):
            if i > 0:
                prev_largest[i] = max(prev_largest[i-1], height[i-1])
        
        for i in range(len(height)-1, 0, -1):
            if i < len(height) - 1:
                next_largest[i] = max(next_largest[i+1], height[i+1])
        
        res = 0
        for i in range(len(height)):
            top = min(next_largest[i], prev_largest[i])
            water = max(top - height[i], 0)
            res += water
        return res