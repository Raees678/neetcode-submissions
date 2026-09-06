from functools import cache

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
            
        n = len(gas)

        running_delta = 0
        candidate_start = 0

        for i in range(n):
            delta = gas[i] - cost[i]
            running_delta += delta

            if running_delta < 0:
                candidate_start = i + 1
                running_delta = 0

        
        return -1 if candidate_start == n else candidate_start
            



        
