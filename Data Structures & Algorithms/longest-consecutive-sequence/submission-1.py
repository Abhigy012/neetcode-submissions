class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(not(len(nums))): 
            return 0
        st = {nums[0]}
        for i in range (1, len(nums)):
            st.add(nums[i])
        currl , maxl = 0,0
        for x in st:
            if (x-1) not in st:
                while x in st:
                    currl += 1
                    x += 1
                maxl = max(currl, maxl)
                currl = 0
        return maxl