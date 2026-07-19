# ABBA
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def valid(char_counts):
            max_index = max(range(len(char_counts)), key=char_counts.__getitem__)
            count = 0
            for i in range(len(char_counts)):
                if i != max_index:
                    count += char_counts[i]
            return count <= k


        i = 0
        res = 0
        char_counts = [0] * 26
        for j in range(len(s)):
            char_counts[ord(s[j]) - ord('A')] += 1

            while not valid(char_counts):
                char_counts[ord(s[i]) - ord('A')] -= 1
                i += 1
            
            curr_len = j - i + 1
            res = max(curr_len, res)
        
        return res




