# 214. Shortest Palindrome
# https://leetcode.com/problems/shortest-palindrome/

class Solution:
    # 找出从头开始的最长回文，将回文右半部分reverse之后贴到前面
    # 比如abcd，从头开始的最长回文是a，所以将bcd转置之后放到a前面，就能得到最短回文：dcbabcd
    def shortestPalindrome(self, s: str) -> str:
        def isPalindrome(str):
            if str==str[::-1]:
                return True
            return False
            
        def reverse(str):
            return str[::-1]
        
        if isPalindrome(s):
            return s
        
        max_len = 0
        for i in range(len(s)):
            if isPalindrome(s[:i]):
                max_len = i
                
        # print(max_len)
        return reverse(s[max_len:])+s
    
