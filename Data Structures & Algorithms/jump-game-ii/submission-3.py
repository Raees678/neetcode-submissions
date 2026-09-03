class Solution:
    def jump(self, nums: List[int]) -> int:
        current_end = 0
        next_end = 0
        jumps = 0

        # visit i if it can be visited using auxiliary state, 
        # each i visited just once,
        # at each visit update the auxillary state that affect future i's visits
        i = 0
        while i < len(nums):
            if i <= current_end:
                # i is reachable within the current number of jumps
                # update the range of i's visitable within one jump
                next_end = max(next_end, i + nums[i])
                i += 1
            else:
                # i is not reachable within the current number of jumps
                # make one jump and set current_end = next_end
                current_end = next_end
                jumps += 1

        return jumps if i == len(nums) else -1
        


