class Solution:
    def rob(self, nums: List[int]) -> int:
        def robLinear(numsLinear):
            n = len(numsLinear)
            dp = [-1] * (n + 1)
            dp[0], dp[1] = 0, numsLinear[0]
        
            for i in range(n+1):
                if dp[i] != -1:
                    continue
                else:
                    dp[i] = max(numsLinear[i-1]+dp[i-2], dp[i-1])
        
            return dp[-1]
        if len(nums) == 1:
            return nums[0]
        return max(robLinear(nums[1:]), robLinear(nums[:-1]))
        