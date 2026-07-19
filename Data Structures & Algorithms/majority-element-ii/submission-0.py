class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        c = Counter(nums)
        for num in c:
            count = c[num]
            buckets[count].append(num)
        res = []
        
        for idx in range(int(len(nums)/3) + 1, len(nums) + 1):
            res.extend(buckets[idx])
        
        return res
