class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def compare(d1, d2):
            # all keys of d1 must be in d2
            # and d2 has as many or more of them
            for k in d1:
                if d1[k] > d2[k]:
                    return False
            return True

        dt = dict(Counter(t))

        i = 0
        ds = defaultdict(int)
        res = float("inf")
        resval = ""
        for j in range(len(s)):
            ds[s[j]] += 1
            while compare(dt, ds):
                # try to shrink until it fails 
                # marking a new best shortest each time
                curr = j - i + 1
                if curr < res:
                    res = curr
                    resval = s[i:j+1]
                ds[s[i]] -= 1
                i += 1
        
        while i < j:
            curr = j - i + 1
            if compare(dt, ds):
                res = curr
                resval = s[i:j+1]
            ds[s[i]] -= 1
            i += 1
                
        return resval

            


        



