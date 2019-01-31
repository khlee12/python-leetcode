# 686. Repeated String Match
# https://leetcode.com/problems/repeated-string-match/

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A) < 1 or len(A) > 10000 or len(B) < 1 or len(B) > 10000:
            return -1
        # start from n which makes the length of a equal or longer than the length of b
        start_time = len(B)//len(A)
        result = A*start_time
        counter = start_time
        
        while(len(result) <= 10000):
            if B in result:
                return counter
            
            counter += 1
            result = A*counter
        return -1
        
        
