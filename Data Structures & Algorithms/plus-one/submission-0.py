class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int(len(digits))
        rem = 1
        for i in range(n-1, -1 , -1):
            curr = int(digits[i]) + rem
            rem = int(curr/10)
            digits[i] = int(curr%10)
        if rem:
            digits = [rem] + digits
        return digits
