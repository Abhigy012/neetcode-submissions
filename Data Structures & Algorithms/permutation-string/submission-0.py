class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for l in range(0 , len(s2) - len(s1) + 1):
            x = s2[l : l+len(s1)]
            if(s1 == sorted(x)):
                return True
        return False