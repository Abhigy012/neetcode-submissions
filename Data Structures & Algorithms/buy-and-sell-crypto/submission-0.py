class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, currb = 0,prices[0]
        for x in range (0, len(prices)):
            price = prices[x]
            if price < currb:
                currb = price
            else:
                maxP = max(maxP, price - currb)
        return maxP
