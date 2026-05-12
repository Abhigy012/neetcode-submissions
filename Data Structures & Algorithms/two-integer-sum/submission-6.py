
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = dict()
        for x in range(len(nums)):
            if mpp.get(target - nums[x]) == None:
                mpp[nums[x]] = x
            else:
                return [mpp[target-nums[x]], x]
        return [-1,-1]

