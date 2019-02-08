# 277. Find the Celebrity
# https://leetcode.com/problems/find-the-celebrity/

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in range(1, n):
            if not knows(i, candidate):
                candidate = i
        
        for i in range(n):
            if i != candidate and ((not knows(i, candidate)) or (knows(candidate, i))):
                return -1
        
        return candidate
