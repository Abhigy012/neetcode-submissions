class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mpp = {}
        for x in nums:
            if mpp.get(x) == None:
                mpp[x] = 1
            else:
                return True
        return False
        