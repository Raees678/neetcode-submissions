class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        for s, e in intervals:
            if res and res[-1][0] <= s <= res[-1][1]:
                res[-1][0] = min(res[-1][0], s)
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])
        
        return res
        