class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val is None or val < min_val:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1] if len(self.stack) > 0 else None
        
