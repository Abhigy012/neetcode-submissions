class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}
        for i in strs:
            x = ''.join(sorted(i))
            if mpp.get(x) == None:
                mpp[x] = []
            mpp[x].append(i)
        result = []
        for st in mpp.values():
            result.append(st)
        return result