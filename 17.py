
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:12:55 2018
@author: khlee
"""

class Solution:
    def __init__(self):
        self = None
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if digits is None or not digits:
            return result
        
        digits_to_str={
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        left_vector = []
        for i in range(len(digits)):
            if not (digits[i] in digits_to_str):
                continue
            if not left_vector:
                left_vector= digits_to_str[digits[i]]
                continue
            right_vector = digits_to_str[digits[i]]
            multiplied_temp = self.multipleString(left_vector, right_vector)
            left_vector = multiplied_temp
            
        result = left_vector
        return result
    
    def multipleString(self, left, right):
        result = []
        for left_char in left:
            for right_char in right:
                result.append(left_char + right_char)
        return result  
        
solution = Solution()
# 测试集
print(len(solution.letterCombinations('')))
print(len(solution.letterCombinations('23')))
print(len(solution.letterCombinations('1234')))
print(len(solution.letterCombinations('1555*#')))
