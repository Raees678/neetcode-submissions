from collections import deque

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        unmerged = []
        res = []

        i = 0
        interval_added = False
        while i < len(intervals):
            curr_s, curr_e = intervals[i]
            new_s, new_e = newInterval
            if interval_added or curr_s < new_s:
                unmerged.append([curr_s, curr_e])
                i += 1
            else:
                unmerged.append([new_s, new_e])
                interval_added = True
        
        if not interval_added:
            unmerged.append(newInterval)

        for i in range(len(unmerged)):
            curr_s, curr_e = unmerged[i]

            if len(res) == 0 or curr_s > res[-1][1]:
                res.append([curr_s, curr_e])
            else:
                res[-1][0] = min(res[-1][0], curr_s)
                res[-1][1] = max(res[-1][1], curr_e)
        
        return res


        
