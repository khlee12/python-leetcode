# 188. Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54113/A-Concise-DP-Solution-in-Java

class Solution:
    def maxProfit(self, k: 'int', prices: 'List[int]') -> 'int':
        if k == 0 or not prices or prices is None:
            return 0
        if k >= len(prices):
            i = 1
            max_profit = 0
            while i < len(prices):
                if prices[i] > prices[i-1]:
                    max_profit += prices[i]-prices[i-1]
                i += 1
            return max_profit
            
        buy_k = [-sys.maxsize]*k
        sell_k = [0]*k
    
        for each_price in prices:
            buy_k[0] = max(buy_k[0], -each_price)
            sell_k[0] = max(sell_k[0], buy_k[0]+each_price)
            for i in range(1, k):
                buy_k[i] = max(buy_k[i], sell_k[i-1]-each_price)
                sell_k[i] = max(sell_k[i], buy_k[i]+each_price)
            # print('buy_k'+str(buy_k))
            # print(sell_k)
        # print(buy_k)
        # print(sell_k)
        return sell_k[-1]
