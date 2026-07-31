class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def comb(i, buffer, buffer_sum):
            if buffer_sum == target:
                res.append(buffer.copy())
                return
            if buffer_sum > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                buffer.append(candidates[j])
                comb(j+1, buffer, buffer_sum + candidates[j])
                buffer.pop()
        
        comb(0, [], 0)
        return res