from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter can be used to count but it doesnt order its elements
        count = Counter(nums)
    
        # create buckets of all the frequencies from 1 to n
        buckets = [[] for i in range(len(nums) + 1)]

    
        for el, count in count.items():
            buckets[count].append(el)

        idx = len(nums)
        res = []
        while k > 0 and idx > 0:
            n = len(buckets[idx])
            res.extend(buckets[idx])
            k -= n
            idx -= 1

        return res
        
