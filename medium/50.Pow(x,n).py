# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1;
        if n < 0:
            n = -n;
            x = 1/x;
        return x*self.myPow(x, n-1) if n%2 else self.myPow(x*x, n/2)
        
