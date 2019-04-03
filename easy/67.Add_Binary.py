# 67. Add Binary
# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        ptr1 = len(a)-1
        ptr2 = len(b)-1
        flag = 0
        while ptr1>=0 or ptr2>=0:
            bitA = int(a[ptr1]) if ptr1 >= 0 else 0
            bitB = int(b[ptr2]) if ptr2 >= 0 else 0
            
            temp = bitA+bitB+flag
            
            # 两个bit相加一共有四种结果
            if temp == 0 or temp == 1:
                result = str(temp)+result
                flag = 0
            elif temp == 2:
                result = '0'+result
                flag = 1
            elif temp == 3:
                result = '1'+result
                flag = 1
            ptr1 -= 1
            ptr2 -= 1
        return result if flag == 0 else '1'+result
