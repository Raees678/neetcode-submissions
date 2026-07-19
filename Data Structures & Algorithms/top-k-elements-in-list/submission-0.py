from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter can be used to count but it doesnt order its elements
        count = Counter(nums)
    
        # create buckets of all the frequencies from 1 to n
        buckets = [None] * len(nums)

    
        for el, count in count.items():
            if buckets[count - 1] is not None:
                buckets[count - 1].append(el)
            else:
                buckets[count - 1] = [el]

        idx = len(nums) - 1
        res = []
        while k > 0 and idx >= 0:
            if buckets[idx] is None:
                idx -= 1
            else:
                n = len(buckets[idx])
                res.extend(buckets[idx])
                k -= n
                idx -= 1

        return res
        
