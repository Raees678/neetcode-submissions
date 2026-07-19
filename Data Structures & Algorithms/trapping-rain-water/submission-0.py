# O(n) time, O(n) space
class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0]
        best = 0
        for h in height:
            best = max(best, h)
            pre.append(best)
        
        post = [0]
        best = 0
        for h in reversed(height):
            best = max(best, h)
            post.append(best)
        post.reverse()

        print(pre)
        print(post)
        res  = 0
        for i, h in enumerate(height):
            res += max(min(pre[i], post[i]) - h, 0)
        
        return res


        