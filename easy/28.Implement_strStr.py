# 28. Implement strStr()
# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or haystack is None:
            if haystack == needle:
                return 0
            return -1
        if not needle or needle is None:
            return 0
        
        # loop, find substring, return index
        sub_str = ' '+haystack[:len(needle)-1]
        
        for i in range(len(needle)-1, len(haystack)):
            sub_str = sub_str[1:]+haystack[i]
            if sub_str == needle:
                return i-len(needle)+1
            
        return -1
