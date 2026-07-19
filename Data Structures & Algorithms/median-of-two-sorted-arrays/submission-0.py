class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # when indexing into 2 lists, keep the shorter list first
        # using a set of paired indices
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = math.ceil(total / 2) # rounds up

        # search for number of elements to take from nums1 = i
        # j = half - i
        l = 0
        r = m
        while l <= r:
            i = (l + r) // 2
            j = half - i
            # last num taken from nums1
            l1 = nums1[i - 1] if i > 0 else float("-inf") 
            # first num not taken from nums2
            r2 = nums2[j] if j < len(nums2) else float("inf")
            if l1 > r2:
                r = i - 1
            else:
                l = i + 1
        
        i = l - 1
        j = half - i
        l1 = nums1[i - 1] if i > 0 else float("-inf") 
        l2 = nums2[j - 1] if j > 0 else float("-inf") 
        r1 = nums1[i] if i < len(nums1) else float("inf")
        r2 = nums2[j] if j < len(nums2) else float("inf")

        if total % 2 == 0:
            return (max(l1, l2) + min(r1, r2)) / 2
        else:
            return max(l1, l2)
        
        




            
        

