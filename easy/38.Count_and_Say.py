# 38. Count and Say
# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        s = self.countAndSay(n-1)
        
        prev = s[0]
        count = 1
        result = ''
        for i in range(1, len(s)):
            if s[i] != prev:
                result += str(count)+prev
                prev = s[i]
                count = 1
            else:
                count += 1
        
        return result+str(count)+prev
