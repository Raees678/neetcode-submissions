class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # find the last index of every character
        idx = {}
        for i in range(len(s)):
            idx[s[i]] = i
        
        curr = prev = last = 0
        res = []
        while curr < len(s):
            last = max(last, idx[s[curr]])
            curr += 1
            if curr > last:
                res.append(last - prev + 1)
                prev = last = curr
        
        return res




