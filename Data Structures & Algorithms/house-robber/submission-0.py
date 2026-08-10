class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n + 1)
        dp[0], dp[1] = 0, nums[0]
        
        for i in range(n+1):
            if dp[i] != -1:
                continue
            else:
                dp[i] = max(nums[i-1]+dp[i-2], dp[i-1])
        
        return dp[-1]
        