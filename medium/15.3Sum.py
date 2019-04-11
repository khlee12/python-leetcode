# 15. 3Sum
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        N = len(nums)
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            target = -nums[i]
            lo = i+1 # important
            hi = N-1
            while lo < hi:
                _sum = nums[lo] + nums[hi]
                if _sum == target:
                    result.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                else:
                    if _sum<target:
                        lo += 1
                    else:
                        hi -= 1
        return result
        
