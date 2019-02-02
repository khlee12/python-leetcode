# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i if i>0 else 0
            else:
                i += 1
        return i
