# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # 现在房子排成了一个圆圈，抢第一个屋子就不能抢最后一个屋子，抢最后一个屋子就不能抢第一个屋子。
        #解法：还是动态规划DP，分别算出这两个条件下的最大抢劫金额，然后取更大的就行。
        # https://www.cnblogs.com/lightwindy/p/8648411.html
        def calculateMax(nums):
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            # print(dp)
            return dp[-1]
        
        
        return max(calculateMax(nums[:-1]), calculateMax(nums[1:]))
