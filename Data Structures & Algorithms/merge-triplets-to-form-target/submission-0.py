class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        eliminated = 0
        found = [False] * 3
        for i in range(len(triplets)):
            skip = False
            for j in range(0, 3):
                if triplets[i][j] > target[j]:
                    eliminated += 1
                    skip = True
                    continue
            
            if skip:
                continue

            for j in range(0, 3):
                if triplets[i][j] == target[j]:
                    found[j] = True
        
        return eliminated < len(triplets) and all(found)