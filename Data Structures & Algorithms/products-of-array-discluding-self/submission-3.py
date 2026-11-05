class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for num in nums:
            pre.append(pre[-1] * num)
        
        pre = pre[:len(pre) - 1]
        post = [1]
        for num in reversed(nums):
            post.append(post[-1] * num)
        post = list(reversed(post[:len(post) - 1]))

        res = []
        for i in range(len(nums)):
            res.append(pre[i] * post[i])
        return res