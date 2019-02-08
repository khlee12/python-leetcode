# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if nums is None or not nums:
            return 0
        pointer = 1
        max_count = 2
        counter = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                if counter < max_count:
                    counter += 1
                else:
                    continue
            else:
                counter = 1
                prev = nums[i]
            nums[pointer], nums[i] = nums[i], nums[pointer]
            pointer += 1
        
        return pointer
            
