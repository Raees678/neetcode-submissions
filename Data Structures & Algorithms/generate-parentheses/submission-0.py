class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        parens = ["(", ")"]
        counts = [n, n]

        def perm(open, closed):
            nonlocal n
            if len(path) == 2*n:
                res.append("".join(path))
                return

            for j in range(0, len(parens)):
                curr = parens[j]
                new_open, new_closed = open, closed
                if curr == "(":
                    new_open += 1
                else:
                    new_closed += 1
                if counts[j] > 0:
                    if curr == ")" and open <= closed:
                        continue

                    counts[j] -= 1
                    path.append(curr)
                    perm(new_open, new_closed)
                    counts[j] += 1
                    path.pop()
        
        perm(0, 0)
        return res


                

            
