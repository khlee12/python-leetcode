# 256. Paint House
# https://leetcode.com/problems/paint-house/

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        '''
        0: red
        1: blue
        2: green
        dp[i][0] = costs[i][0]+min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = costs[i][1]+min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2]+min(dp[i-1][0], dp[i-1][1])
        '''
        if not costs:
            return 0
        houses = len(costs)
        dp = [[0 for i in range(3)] for i in range(houses)]
        dp[0] = costs[0]
        for i in range(1, houses):
            dp[i][0] = costs[i][0]+min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i][1]+min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i][2]+min(dp[i-1][0], dp[i-1][1])
        
        return min(dp[-1][0], dp[-1][1], dp[-1][2])
