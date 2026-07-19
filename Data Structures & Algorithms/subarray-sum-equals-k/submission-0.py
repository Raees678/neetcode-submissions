class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        prefix_sums = []
        for num in nums:
            sum += num
            prefix_sums.append(sum)
        
        d = defaultdict(int)
        res = 0
        for ps in prefix_sums:
            diff = ps - k
            if diff == 0:
                res += 1
            res += d[diff]
            d[ps] += 1
        
        print(d)
        return res
