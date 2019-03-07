# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, s: str) -> int:
        power = len(s)-1
        result = 0
        for i in range(len(s)):
            result += pow(26, power)*(ord(s[i])-ord('A')+1)
            power -= 1
            
        return result
