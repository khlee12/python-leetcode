# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # One can reach i^{th} step in one of the two ways:
        #   1. Taking a single step from (i-1)^{th} step.
        #   2. Taking a step of 2 from (i-2)^{th} step.
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0]*(n)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
