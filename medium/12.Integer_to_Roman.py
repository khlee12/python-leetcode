# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        _char = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        _num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ''
        pointer = 0
        while num > 0:
            while num >= _num[pointer] and pointer<len(_num):
                num -= _num[pointer]
                result += _char[pointer]
            pointer += 1
            
        return result
