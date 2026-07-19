class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        d1 = defaultdict(int)
        for c in s1:
            d1[c] += 1
        
        i = 0
        d2 = defaultdict(int)
        for j in range(len(s2)):
            print("j", j)
            # expand the window
            d2[s2[j]] += 1
            # if its bigger than len(s1) shrink it so you
            # always have a window exactly equal to len(s1)
            while j - i + 1 > len(s1):
                d2[s2[i]] -= 1
                i += 1
                print("i", i)
            
            all_nums_equal = True
            for c in d1.keys():
                if d1[c] != d2[c]:
                    all_nums_equal = False
                    break
            
            if all_nums_equal:
                return True

        
        return False

