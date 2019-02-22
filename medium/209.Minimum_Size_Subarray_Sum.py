# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, s: 'int', nums: 'List[int]') -> 'int':
        if not nums or nums is None:
            return 0
        
        result = sys.maxsize
        _sum = 0
        left_pointer = 0
        for i in range(len(nums)):
            _sum += nums[i]
            while _sum >= s:
                result = min(result, i-left_pointer+1)
                _sum -= nums[left_pointer]
                left_pointer += 1
        return result if result != sys.maxsize else 0
