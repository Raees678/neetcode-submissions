class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_seen = defaultdict(lambda: -1)
        i = 0
        res = 0
        d = defaultdict(int)

        for j in range(len(s)):
            c = s[j]
            while c in d:
                del d[s[i]]
                i += 1
            
            d[c] = j 
            curr_len = j - i + 1
            res = max(curr_len, res)
        
        return res


        




        