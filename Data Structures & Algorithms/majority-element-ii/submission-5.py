class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # The key insight to O(1) space is that there cannot be more than 2 elements
        # that appear more than n/3 times. Why?
        # If 2 elements both appear (n+1)/3 times out of n elements, then the remainder
        # is (n-2)/3 elements left. Even if all these elements are the same this still
        # wont be a majority element.

        def boyer_moore():
            curr1 = curr2 = None
            count1 = count2 = 0
            
            for num in nums:
                if count1 == 0:
                    curr1 = num
                elif count2 == 0:
                    curr2 = num
                
                if num == curr1:
                    count1 += 1
                elif num == curr2:
                    count2 += 1
                else:
                    count1 -= 1
                    count2 -= 1
            
            total_count1 = total_count2 = 0
            for num in nums:
                if num == curr1:
                    total_count1 += 1
                elif num == curr2:
                    total_count2 += 1

            return curr1, total_count1, curr2, total_count2


        num1, count1, num2, count2 = boyer_moore()
        # print(num1, count1)
        # print(num2, count2)
        # print(len(nums) // 3)

        
        res = []
        if num1 is not None and count1 > len(nums) // 3:
            res.append(num1)
        if num2 is not None and count2 > len(nums) // 3:
            res.append(num2)
        
        return res

        
        
    