class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        low , high = 0, len(nums)-1
        while low < high:
            if(nums[low] < nums[high]):
                return nums[low]
            mid = int(low + (high-low)/2)
            if nums[low] <= nums[mid]:
                low = mid+1
            else:
                high = mid
        return nums[high]
