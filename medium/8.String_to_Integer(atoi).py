# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, str: str) -> int:
        MIN = -2147483648
        MAX = 2147483647
        
        num = str.strip()
        if not num:
            return 0
        
        if num[0] != '+' and num[0] !='-' and not num[0].isnumeric():
            return 0
        
        start = 1 if num[0]=='+' or num[0]=='-' else 0
        ptr = start
        while ptr < len(num):
            if not num[ptr].isnumeric():
                break
            ptr += 1
        
        if ptr==start:
            return 0
        
        result = int(num[:ptr])
        if result < MIN:
            return MIN
        elif result > MAX:
            return MAX
        return result
