# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        
        if not 1 in nums:
            return 1
        if len(nums) == 1 and nums[0] == 1:
            return 2
        
        # 将不符合【首个缺失的正整数】范围的数，换成default value，在这里是0
        # 【首个缺失的正整数】范围：1～n+1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
            
        # 如果这个数出现过，则将arr[exist]设为负数（与原数组不一样的属性）
        for i in range(len(nums)):
            exist = abs(nums[i])
            nums[exist-1] = - abs(nums[exist-1])
            
        # 第一个不满足上面条件的数（即正数），为首个缺失的正整数
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        
        return len(nums)+1
