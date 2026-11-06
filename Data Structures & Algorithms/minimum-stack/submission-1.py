class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        prev_min = float("inf") if not self.mins else self.mins[-1]
        curr_min = min(prev_min, val)
        self.mins.append(curr_min)
        
    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mins[-1]
        
