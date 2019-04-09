# 367. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==0:
            return True
        lo = 0
        hi = num
        
        while lo < hi:
            mid = lo+(hi-lo)//2+1
            if mid*mid <= num:
                lo = mid
            else:
                hi = mid-1
        if lo*lo == num:
            return True
        return False
