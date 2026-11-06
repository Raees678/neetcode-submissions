class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            first, second = numbers[i], numbers[j]
            if first + second == target:
                return [i+1, j+1]
            elif first + second > target:
                j -= 1
            elif first + second < target:
                i += 1
        
        raise Exception("There is always one valid solution")