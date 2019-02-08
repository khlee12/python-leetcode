# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        start = 0
        while count < len(nums):
            _prev = nums[start]
            current = start
            while True:
                _next = (current+k)%len(nums)
                nums[start], nums[_next] = nums[_next], nums[start]
                current = _next
                count += 1
                if current == start:
                    break
            start += 1
        
