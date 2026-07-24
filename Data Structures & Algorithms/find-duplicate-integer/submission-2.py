# [0,0,2]
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # this is a linked list cycle detection problem given as a list
        # instead of nodes you have indices
        # instead of pointers the numbers are the index of the next elem

        # each elem is between 1 and n so they are all in range
        
        slow = fast = 0
        while True:
            # since you are guaranteed a cycle, these must meet
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # index of the entrypoint is the dup element
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow            
            

