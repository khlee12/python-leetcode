# 27.Remove Element
# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        non_val_pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[non_val_pointer], nums[i] = nums[i], nums[non_val_pointer]
                non_val_pointer += 1
        
        return non_val_pointer
