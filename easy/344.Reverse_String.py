# 344. Reverse String
# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s or s is None:
            return 
        
        # reverse array
        left = 0
        right = len(s)-1
        
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
