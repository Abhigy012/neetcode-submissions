class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix , i = 1, 0
        pref = []
        while i < len(nums):
            prefix *= nums[i]
            pref.append(prefix)
            i += 1
        i = len(nums) - 1
        res = []
        suff = 1
        while i>= 0:
            if i == len(nums) - 1:
                res.append(pref[i-1])
            elif i == 0:
                res.append(suff)
            else:
                res.append(pref[i-1] * suff)
            suff *= nums[i]
            i -= 1
        res.reverse()
        return res
