# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or not prices or len(prices) == 1:
            return 0
        
        min_price = prices[0]
        profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = max(profit, price-min_price)
        
        return profit
