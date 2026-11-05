class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append(":")
            res.append(s)
        
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        i = j = 0
        res = []
        while i < len(s) and j < len(s):
            while s[j] != ":":
                j += 1
            length = int(s[i:j])
            
            subs = s[j+1 : j+1+length]
            res.append(subs)
            i = j + 1 + length
            j = i

        return res

