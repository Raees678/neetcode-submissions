class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_s, new_e = newInterval
        added = False

        
        for i in range(len(intervals)):
            s, e = intervals[i]
            # either add or merge new_interval into res if its time
            if not added and new_s < s:
                if res and res[-1][0] <= new_s <= res[-1][1]:
                    res[-1][0] = min(res[-1][0], new_s)
                    res[-1][1] = max(res[-1][1], new_e)
                else:
                    res.append([new_s, new_e])
                added = True
            
            # either add or merge [s,e] into res
            if res and res[-1][0] <= s <= res[-1][1]:
                res[-1][0] = min(res[-1][0], s)
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])

        if not added:
            if res and res[-1][0] <= new_s <= res[-1][1]:
                res[-1][0] = min(res[-1][0], new_s)
                res[-1][1] = max(res[-1][1], new_e)
            else:
                res.append([new_s, new_e])

        return res

            
                
            


