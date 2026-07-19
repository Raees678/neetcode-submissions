class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for num in nums:
            val = pre[-1] * num
            pre.append(val)
        pre = pre[:len(pre) - 1]

        post = [1]
        for num in reversed(nums):
            print(num)
            val = post[-1] * num
            post.append(val)
        post = post[:len(post) - 1]
        post = list(reversed(post))

        res = []
        for (pre_num, post_num) in zip(pre, post):
            res.append(pre_num * post_num)
        
        return res




