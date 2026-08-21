class Solution:
    def jump(self, i:int, nums:List[int], dp : List[int]) -> bool:
        if dp[i] != -1:
            return dp[i]
        for x in range(i+1, i+nums[i]+1):
            if ((x+1) >= len(nums) or (self.jump(x, nums,dp))):
                dp[i] = 1
                break
        if dp[i] == -1 :
            dp[i] = 0
        return dp[i]
        
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp = [-1] * n
        # dp[n-1] = 1
        # return bool(self.jump(0,nums,dp))
        vis = [False]*n
        vis[0] = True
        for i in range(n):
            if not vis[i]:
                return False
            for x in range(i+1 , i+nums[i]+1):
                if (x+1 >= n):
                    vis[n-1] = True
                    break
                vis[x] = 1
        return vis[n-1]