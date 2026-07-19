class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        dq = deque()
        res = []

        for j in range(len(nums)):
            if j - i + 1 > k:
                res.append(nums[dq[0]])
                if dq[0] <= j - k:
                    dq.popleft()
                i += 1

            while dq and nums[dq[-1]] <= nums[j]:
                dq.pop()
                
            dq.append(j)
        
        if dq:
            res.append(nums[dq[0]])

        return res
        


