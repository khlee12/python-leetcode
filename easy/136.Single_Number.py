# 136. Single Number
# https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bit manipulation
        # XOR!!!!!!!
        # a xor a = 0
        # a xor 0 = a
        # a xor b xor a = (a xor a) xor b
        result = 0
        for i in nums:
            result ^= i
        return result
