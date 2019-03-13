# 65. Valid Number
# https://leetcode.com/problemset/all/?search=65

class Solution:
    def isNumber(self, s: str) -> bool:
        # 正/负整数
        # 正/负浮点数
        # 正/负整数e正/负整数
        # 正/负浮点数e正/负整数
        def isInteger(str):
            _str = str.strip()
            if not _str or _str is None:
                return False
            if _str == '+' or _str == '-':
                return False
            for i in range(len(_str)):
                if _str[i] == '+' or _str[i] == '-':
                    if i != 0:
                        return False
                    else:
                        continue
                if _str[i] > '9' or _str[i] < '0':
                    return False
            return True
        
        def isFloat(str):
            _str = str.strip()
            if '.' in _str:
                arr = _str.split('.')
                if len(arr) != 2:
                    return False
                if not arr[0] and not  arr[1]:
                    return False
                if not arr[0] and arr[1]:
                    if arr[1][0] >= '0' and arr[1][0] <= '9' and isInteger(arr[1]):
                        return True
                if arr[0] and not arr[1]:
                    if isInteger(arr[0]):
                        return True
                if (isInteger(arr[0]) or (arr[0]=='+' or arr[0] == '-')) and isInteger(arr[1]):
                    return True
            else:
                return False
            return False
                    
        stripped = s.strip()
        if ' ' in stripped:
            return False
        
        if 'e' in stripped:
            arr = stripped.split('e')
            
            if len(arr) != 2:
                return False
            
            if (isInteger(arr[0]) and isInteger(arr[1])) or (isFloat(arr[0]) and isInteger(arr[1])):
                
                return True
        else:
            if isInteger(s) or isFloat(s):
                return True
        
        return False
