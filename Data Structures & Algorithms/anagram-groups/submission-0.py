from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        
        res = list(d.values())
        return res
        