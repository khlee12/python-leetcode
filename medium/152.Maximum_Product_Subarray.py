# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
# https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity

class Solution:
    def maxProduct(self, nums: 'List[int]') -> 'int':
        # 用imin和imax存储每个状态的最小值和最大值
        imin = nums[0]
        imax = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                imin, imax = imax, imin
            if nums[i] == 0:
                imin, imax = 0, 0
            imin = min(imin*nums[i], nums[i])
            imax = max(imax*nums[i], nums[i])
            result = max(result, imax)
            # print(str(imin)+" "+str(imax))
        return result
        
