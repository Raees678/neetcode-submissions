class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s):03}")
            res.append(s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        curr = 0
        while curr < len(s):
            l = int(s[curr:curr + 3])
            curr += 3
            string = s[curr:curr + l]
            curr += l
            res.append(string)
        
        return res

