# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        if not nums or nums is None:
            return []
        if len(nums) == 1:
            return nums
        output = [1]
        _p = 1
        for i in range(len(nums)-1):
            _p *= nums[i]
            output.append(_p)
        
        _p = 1
        for i in range(len(nums)-1, 0, -1):
            _p *= nums[i]
            output[i-1] *= _p
        
        return output
