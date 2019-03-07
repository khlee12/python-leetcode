# 246. Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        _s = {
            '0': '0',
            '1': '1',
            '2': None,
            '3': None,
            '4': None,
            '5': None,
            '6': '9',
            '7': None,
            '8': '8',
            '9': '6'
        }
        result = ''
        for i in range(len(num)-1, -1, -1):
            if _s[num[i]] is None:
                return False
            result += _s[num[i]]
        if result == num:
            return True
        return False
        
