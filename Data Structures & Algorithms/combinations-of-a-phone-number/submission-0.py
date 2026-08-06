class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []
        path = []

        def rec(i):
            if i == len(digits):
                res.append("".join(path))
                return

            for letter in d[digits[i]]:
                path.append(letter)
                rec(i+1)
                path.pop()
            
        rec(0)
        return res
        

