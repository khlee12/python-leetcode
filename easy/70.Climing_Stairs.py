# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 斐波那契数列
        # f(n) = f(n-1)+f(n-2)
        # f(1) = 1
        # f(2) = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        # 递归 -> 无法通过og
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        # 循环
        # fib = [0]*(n+1)
        # fib[1] = 1
        # fib[2] = 2
        # for i in range(3, n+1):
        #     fib[i] = fib[i-1] + fib[i-2]  
        # return fib[n]
    
        # from Solution
        # 每次更新相加的两个数
        # BEST，时间和空间复杂度最低
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second
            
        
