# 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> 'bool':
        min_val = sys.maxsize
        mid_val = sys.maxsize
        
        for each_num in nums:
            if each_num <= min_val:
                min_val = each_num
            elif each_num <= mid_val:
                mid_val = each_num
            else:
                return True
            
        return False
            
