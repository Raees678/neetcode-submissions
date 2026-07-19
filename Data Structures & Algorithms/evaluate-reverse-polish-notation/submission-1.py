class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_operator(c):
            return c in ["+", "-", "*", "/"]
        
        def operate(c, num_1, num_2):

            if c == "+":
                return num_1 + num_2
            elif c == "-":
                return num_1 - num_2
            elif c == "*":
                return num_1 * num_2
            elif c == "/":
                return int(num_1 / num_2)

                
        stack = []
        for t in tokens:
            if not is_operator(t):
                stack.append(t)
            else:
                num_2 = int(stack.pop())
                num_1 = int(stack.pop())
                res = operate(t, num_1, num_2)
                stack.append(res)
        
        return int(stack[-1])


        