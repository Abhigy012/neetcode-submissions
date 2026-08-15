class Solution:
    def isHappy(self, n: int) -> bool:
        mpp = {}
        while (mpp.get(n) == None):
            mpp[n] = 1
            x = 0
            while (n > 0):
                x = x + int((n%10)**2)
                n = int(n/10)
            
            if x == 1:
                return True
            n = x
        return False
        