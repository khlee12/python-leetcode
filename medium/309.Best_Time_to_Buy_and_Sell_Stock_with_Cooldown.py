# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if not prices or prices is None or len(prices) < 2:
            return 0
        s0 = [0]
        s1 = [-prices[0]]
        s2 = [0]
        for i in range(1, len(prices)):
            s0.append(max(s0[i-1], s2[i-1]))
            s1.append(max(s1[i-1], s0[i-1]-prices[i]))
            s2.append(s1[i-1]+prices[i])
        return max(s0[-1], s2[-1])
