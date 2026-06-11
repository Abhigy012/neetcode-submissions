class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        result = []
        for i in range(len(temp)-1, -1 , -1):
            while stack and temp[stack[-1]] <= temp[i]:
                stack.pop()
            if not stack:
                result.append(0)
            else:
                result.append(stack[-1] - i)
            stack.append(i)
        for i in range(int(len(result)/2)):
            t = result[i] 
            result[i] = result[len(result) - i - 1]
            result[len(result) - i - 1] = t
        return result