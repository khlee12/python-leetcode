# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, num):
        # 实现26进制 *但26的倍数时，不进位
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[num%26-1])
            num = (num-1)//26
        result.reverse()
        return ''.join(result)
         
