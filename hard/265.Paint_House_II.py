# 265. Paint House II
# https://leetcode.com/problems/paint-house-ii/

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        k = len(costs[0])
        houses = len(costs)
        dp = [[0 for i in range(k)] for j in range(houses)]
        dp[0] = costs[0]
        
        for i in range(1, houses):
            for j in range(k):
                dp[i][j] = costs[i][j]+min(dp[i-1][:j]+dp[i-1][j+1:])

        return min(dp[-1])
