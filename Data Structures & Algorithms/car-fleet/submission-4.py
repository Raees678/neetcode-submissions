class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed))
        times = [(target - p)/s for p,s in pairs]

        stack = []
        for time in times:
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        
        return len(stack)