# 247. Strobogrammatic Number II
# https://leetcode.com/problems/strobogrammatic-number-ii/

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        return self.helper(n, n)
    
    def helper(self, n, m):
        if n==1:
            return ['0', '1', '8']
        if n==2:
            if n!= m:
                return ['00', '11', '88', '69', '96']
            else:
                return ['11', '88', '69', '96']
        _string = self.helper(n-2, m)
        result = []
        for s in _string:
            if n != m:
                result.append('0'+s+'0')
            result.append('1'+s+'1')
            result.append('8'+s+'8')
            result.append('6'+s+'9')
            result.append('9'+s+'6')
        return result
