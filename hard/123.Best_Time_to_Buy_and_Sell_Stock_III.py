# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39615/My-explanation-for-O(N)-solution!

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or prices is None or len(prices) == 1:
            return 0
        
        buy1 = -sys.maxsize
        buy2 = -sys.maxsize
        sell1 = 0
        sell2 = 0
        for each_price in prices:
            buy1 = max(buy1, -each_price)
            sell1 = max(sell1, buy1+each_price)
            buy2 = max(buy2, sell1-each_price)
            sell2 = max(sell2, buy2+each_price)
        
        return sell2
