from collections import defaultdict

# time complexity: O(n), we hit every number in nums exactly once when creating the set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        
        max_seq_len = 0
        for num in nums:
            if num - 1 not in s:
                # num is the first number in the subsequence
                seq_len = 1
                # curr is the first number that we havent seen yet
                # that we hope is also in the subseq
                curr = num + 1
                while curr in s:
                    # we saw curr, increase the seq len
                    seq_len += 1
                    # pick the next number we hope to see
                    curr += 1
                max_seq_len = max(max_seq_len, seq_len)
        
        return max_seq_len


