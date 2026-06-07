class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        for i in range (0, len(heights)):
            if heights[i] == 0:
                continue
            for j in range(i, len(heights)):
                if heights[j] == 0:
                    continue
                currwater = min(heights[i], heights[j]) * (j - i)
                maxWater = max(maxWater, currwater)
        return maxWater
                
