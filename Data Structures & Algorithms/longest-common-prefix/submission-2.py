class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        char_idx = 0
        while True:
            if char_idx < len(strs[0]):
                c = strs[0][char_idx]
            else:
                return strs[0][0:char_idx]

            for s in strs:
                if char_idx >= len(s) or s[char_idx] != c:
                    return strs[0][0:char_idx]
            char_idx += 1
            