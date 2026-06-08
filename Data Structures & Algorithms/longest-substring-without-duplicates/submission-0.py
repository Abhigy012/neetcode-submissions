class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mpp = dict()
        l = 0
        maxL = 0
        for r in range (0, len(s)):
            if (mpp.get(s[r]) == None) or (mpp[s[r]] == 0):
                mpp[s[r]] = 1
                maxL = max(maxL, r - l + 1)
            else:
                while mpp[s[r]] > 0 and l <= r:
                    mpp[s[l]] -= 1
                    l += 1
                mpp[s[r]] += 1
        return maxL