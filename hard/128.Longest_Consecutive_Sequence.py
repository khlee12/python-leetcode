# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> 'int':
        if not nums or nums is None:
            return 0
        # ２。找到连续元素的开端，遍历set直到连续元素结束
        longest_len = 0
        num_set  = set(nums)
        for each_num in nums:
            if each_num-1 not in num_set:
                # 连续元素的开端
                curr_num = each_num
                curr_len = 1
                while curr_num+1 in num_set:
                    curr_num += 1
                    curr_len += 1 
                longest_len = max(longest_len, curr_len)
                
        return longest_len
                
        
#         # １。排序后求最长连续子数组
#         length = 1
#         longest_length = 1
#         nums = sorted(nums)
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i-1]:
#                 if nums[i] == nums[i-1]+1:
#                     length += 1
#                 else:
#                     # start again
#                     longest_length = max(longest_length, length)
#                     length = 1
                    
#         return max(longest_length, length)
