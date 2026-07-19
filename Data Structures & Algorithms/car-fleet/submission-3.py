# canonical solution
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        times = [(target - p)/s for p, s in pairs]

        # pos = [7, 5, 2, 1]
        # tim = [5, 4, 1, 6]
        # 2 fleets: pos 7,5,2 are limited by time=5, then pos 1 comes at time=6
        # keep a monotonically increasing stack of the limiters

        stack = []
        for time in times:
            stack.append(time)
            # only keep the newly appended if its lesser than the previous
            if len(stack) > 1 and stack [-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

