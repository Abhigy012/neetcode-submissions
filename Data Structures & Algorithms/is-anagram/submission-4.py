class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        mpp = dict()
        for x in s:
            if x in mpp:
                mpp[x] += 1
            else:
                mpp[x] = 1

        for x in mpp:
            print(x , " ",mpp[x])

        for y in t:
            if mpp.get(y) == None or mpp[y] == 0:
                return False
            else:
                mpp[y] -= 1
        return True
            