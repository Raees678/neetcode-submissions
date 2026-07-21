# [0,0,2]
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            # since you are guaranteed a cycle, these must meet
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # index of the entrypoint is the dup element
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow            
            

