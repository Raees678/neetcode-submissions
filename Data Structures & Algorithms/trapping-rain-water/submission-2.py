class Solution:
    def trap(self, height: List[int]) -> int:
        # trick 1: the edges will always have 0 water
        l = 0
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        res = 0

        # the height of each block is constrained by
        # the minimum height on its left and right side
        
        # we only need one of these values
        # if we move the left pointer that means that 

        while l < r:
            if max_left <= max_right:
                l += 1
                res += max(max_left - height[l], 0)
            else:
                r -= 1
                res += max(max_right - height[r], 0)

            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])
        
        return res
            

            
