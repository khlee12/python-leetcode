# 165. Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        p1 = 0
        p2 = 0
        def removeZeros(num):
            ptr = 0
            for i in range(len(num)):
                if num[i] != '0':
                    break
                else:
                    ptr += 1
            return num[ptr:] if ptr < len(num) else '0'
        
        while p1<len(v1) or p2<len(v2):
            temp1 = v1[p1] if p1<len(v1) else '0'
            temp2 = v2[p2] if p2<len(v2) else '0'
            
            num1 = removeZeros(temp1)
            num2 = removeZeros(temp2)
            
            if int(num1) < int(num2):
                return -1
            elif int(num1) > int(num2):
                return 1
            
            p1 += 1
            p2 += 1
        
        return 0
