# 448. Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
#         if nums is None or not nums:
#             return []
#         if len(nums) == 1:
#             return []

#         pointer = 1
#         result = []
#         for i in range(1, len(nums)+1):
#             if not i in nums:
#                 result.append(i)

#         return result
# 会出现Time Limit Exceeded错误，因为本质上判断是否在此数组的时间复杂度为O(n)， 所以相当于复杂度O(n^2)

# 以下方法可以通过oj
# 参考：https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/217789/Python-one-liner
        
        return list(set(range(1, len(nums) + 1)) - set(nums))
