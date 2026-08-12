class Solution:
    def reverseBits(self, n: int) -> int:
        res = int(0)
        curr = 2 ** 31
        while n > 0:
            res += (curr *(n & 1))
            curr /= 2
            n = n>>1
        return int(res)