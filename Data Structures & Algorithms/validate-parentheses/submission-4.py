class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        def opening(c: str) -> bool:
            return c == "(" or c == "[" or c == "{"
        
        def closing(c: str) -> bool:
            return c == ")" or c == "]" or c == "}"
        
        def closes(c1: str, c2: str) -> bool:
            return c1 == "(" and c2 == ")" \
                or c1 == "[" and c2 == "]" \
                or c1 == "{" and c2 == "}"

        stack = []
        for c in s:
            if opening(c):
                stack.append(c)
            elif closing(c):
                if len(stack) > 0 and closes(stack[-1], c):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
            
                
        