class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        parens = ["(", ")"]
        counts = [n, n]
        open = closed = 0

        def perm():
            nonlocal n, open, closed
            if len(path) == 2*n:
                res.append("".join(path))
                return

            for j in range(0, len(parens)):
                curr = parens[j]
                if counts[j] > 0:
                    if curr == ")" and open <= closed:
                        continue
                    
                    if curr == "(":
                        open += 1
                    else:
                        closed += 1

                    counts[j] -= 1
                    path.append(curr)
                    perm()
                    counts[j] += 1
                    path.pop()

                    if curr == "(":
                        open -= 1
                    else:
                        closed -= 1

        
        perm()
        return res


                

            
