from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def rec(i):
            if i > len(cost):
                return float("inf")
            if i == len(cost):
                return 0
            
            this_step_cost = cost[i]
            one_step = this_step_cost + rec(i+1)
            two_steps = this_step_cost + rec(i+2)
            return min(one_step, two_steps)
        
        return min(rec(0), rec(1))


