class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mpp = {}
        for i in nums:
            if(mpp.get(i) != None):
                return True
            mpp[i] = i;
        return False