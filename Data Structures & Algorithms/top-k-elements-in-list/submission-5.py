class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [set() for n in range(len(nums) + 1)]

        for num in nums:
            buckets[count[num]].add(num)
        
        i = len(nums)
        res = []
        count = 0
        
        while count < k:
            for el in buckets[i]:
                if count < k:
                    res.append(el)
                    count += 1
                else:
                    return res
            i -= 1
        
        return res

            



        