class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def pred(eating_rate):
            res = 0
            for pile in piles:
                res += math.ceil(pile/eating_rate)
            return res <= h
        
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2
            if pred(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l