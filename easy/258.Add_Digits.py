# 258. Add Digits
# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            # add num
            new_num = 0
            while num > 0:
                new_num += num%10
                num //= 10
            num = new_num
        return num
