# [3, 4.5, 10, 3]

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], (target - position[i]) / speed[i]) for i in range(len(speed))]
        cars.sort()
        stack = []
        for _, t in reversed(cars):
            if stack and t <= stack[-1]:
                continue
            stack.append(t)
        
        return len(stack)
        

            
