class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub = 0
        res = float('-inf')
        for x in nums:
            sub += x
            res = max(res, sub)
            sub = max(0, sub)
        return res