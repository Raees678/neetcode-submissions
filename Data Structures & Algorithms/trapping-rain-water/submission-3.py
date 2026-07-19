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
        
        # we only need one of these values calculated when we
        # reach a certain block as long as we are sure that its 
        # smaller than the other

        # eg. if we know that max_left is less than max_right
        # we know that it will limit the the height of block l + 1
        # no matter how large any other right blocks may be
        # and vica verca for right
        while l < r:
            if max_left <= max_right:
                l += 1
                res += max(max_left - height[l], 0)
                max_left = max(max_left, height[l])
            else:
                r -= 1
                res += max(max_right - height[r], 0)
                max_right = max(max_right, height[r])
        
        return res
            

            
