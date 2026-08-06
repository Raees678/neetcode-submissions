class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        path = []

        def comb(i, path_sum):
            if path_sum == target:
                res.append(path.copy())
                return

            if path_sum > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])
                comb(j+1, path_sum + candidates[j])
                path.pop()
        
        comb(0, 0)
        return res