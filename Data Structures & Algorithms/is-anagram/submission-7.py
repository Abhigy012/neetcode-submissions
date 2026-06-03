class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mpp = {};
        for i in range (0,26):
            mpp[i] = 0
        for i in s:
            mpp[ord(i) - ord('a')] += 1
        for i in t:
            if mpp[ord(i) - ord('a')] == 0:
                return False
            mpp[ord(i) - ord('a')] -= 1
        for i in range (0,26):
            if mpp[i] != 0:
                return False
        return True