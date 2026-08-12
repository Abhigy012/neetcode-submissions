class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arrxor,currxor=0,len(nums)
        for i in range(len(nums)):
            arrxor ^= nums[i]
            currxor ^= i
        print(arrxor, currxor)
        return (arrxor ^ currxor)