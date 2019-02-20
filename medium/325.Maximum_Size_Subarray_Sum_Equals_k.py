# 325. Maximum Size Subarray Sum Equals k
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

class Solution:
    def maxSubArrayLen(self, nums: 'List[int]', k: 'int') -> 'int':
        if not nums or nums is None:
            return 0
        
        arr_sum = 0
        sum_len_hash = {}
        max_size = 0
        for i in range(len(nums)):
            arr_sum += nums[i]
            if arr_sum  == k:
                max_size = max(max_size, i+1)
                sum_len_hash[arr_sum] = min(i, sum_len_hash[arr_sum]) if arr_sum in sum_len_hash.keys() else i
            elif arr_sum-k in sum_len_hash:
                max_size = max(max_size, i-sum_len_hash[arr_sum-k])
            else:
                sum_len_hash[arr_sum] = min(i, sum_len_hash[arr_sum]) if arr_sum in sum_len_hash.keys() else i
        
        return max_size
