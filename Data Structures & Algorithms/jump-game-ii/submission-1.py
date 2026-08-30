class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque([(0, 0)])
        visited = set()
        while q:
            steps, curr = q.popleft()
            if curr == len(nums) - 1:
                return steps

            for next in range(curr + 1, curr + nums[curr] + 1):
                if next not in visited:
                    visited.add(next)
                    q.append((steps+1, next))
        
        return -1
            


            
