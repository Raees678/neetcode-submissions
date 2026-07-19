from collections import defaultdict

# sorting solution nlog(n) time, O(1) space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            nums.sort()

            seq_len = max_seq_len = 0
            prev = None
            for num in nums:
                if num == prev:
                    pass
                elif prev is None or num == prev + 1:
                    seq_len += 1
                else:
                    seq_len = 1
                max_seq_len = max(seq_len, max_seq_len)
                prev = num
            
            return max_seq_len