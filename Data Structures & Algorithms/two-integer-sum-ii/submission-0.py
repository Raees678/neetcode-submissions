# [1,2,3,4], t = 3
# ans [1, 2], idx 1 = 1, idx 2 = 2, sum = 3
# O(1) space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        while low < high:
            s = numbers[low] + numbers[high]
            if s < target:
                low += 1
            elif s > target:
                high -= 1
            else:
                return [low + 1, high + 1]