# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        num = 1
        while num*num <= x:
            num += 1
        return num-1
