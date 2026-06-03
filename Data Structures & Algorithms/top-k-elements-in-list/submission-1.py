class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp = {}
        for i in nums:
            if mpp.get(i) == None:
                mpp[i] = 0
            mpp[i] += 1
        lst = []
        for key,value in mpp.items():
            lst.append([-value, key])
        lst.sort()
        res = []
        for i in range (0,k):
            res.append(lst[i][1])
        return res
        