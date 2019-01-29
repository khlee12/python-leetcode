# 198. House Robber
# https://leetcode.com/problems/house-robber/
# 动态规划
# https://www.youtube.com/watch?v=Jakbj4vaIbE

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 不相邻数字的最大和
        # max(opt(n-2)+new_num, opt(n-1))
        # 动态规划解法
        if nums is None or not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        opt_arr = [0]*len(nums)
        opt_arr[0] = nums[0]
        opt_arr[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            A = opt_arr[i-2]+nums[i]
            B = opt_arr[i-1]
            opt_arr[i] = max(A, B)
            
        return opt_arr[-1]
        # 递归解法
        #return self.opt(nums, len(nums)-1)
        
      
    # def opt(self, nums, i):
    #     if i==0:
    #         return nums[0]
    #     if i==1:
    #         return max(nums[0], nums[1])
    #     else:
    #         return max(self.opt(nums, i-2)+nums[i], self.opt(nums, i-1))
        
