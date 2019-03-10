# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        basic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)-1):
            if basic[s[i]] < basic[s[i+1]]:
                result -= basic[s[i]]
            else:
                result += basic[s[i]]
            
        return result+basic[s[-1]]
