class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the cars by position
        pairs = sorted(zip(position, speed))
        times = [(target - pairs[i][0])/pairs[i][1] for i in range(len(pairs))]
        # if index i has a lower num than index i + 1
        # eg. [... 1, 5, ...]
        # then index i is limited by the num in front of it

        stack = []

        for time in times:
            while len(stack) > 0 and stack[-1] <= time:
                stack.pop()
            # keep only the limiting cars in the stack
            stack.append(time)
        
        # return the limiting cars
        return len(stack)

