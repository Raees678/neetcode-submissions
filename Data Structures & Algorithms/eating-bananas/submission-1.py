class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calcHours(eatingRate):
            res = 0
            for pile in piles:
                res += math.ceil(pile/eatingRate)
            
            return res

        max_per_pile = max(piles)
        
        # either you eat 1 banana per hour 
        # all the way to the max number of bananas per hour
        l = 1
        r = max(piles)

        
        while l <= r:
            mid = (l + r) // 2
            hours = calcHours(mid)
            # you finished much faster, eat less bananas per hour 
            # to get the minimum
            if hours <= h:
                r = mid - 1
            elif hours > h:
                # you didnt finish, eat more
                l = mid + 1
            # else:
            #     # youve reached the limit, any fewer bananas eaten 
            #     # per hour you wont finish, any mroe and you wont find the min
            #     return mid
        
        return l
