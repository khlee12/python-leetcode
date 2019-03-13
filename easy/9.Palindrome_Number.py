# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        return False
