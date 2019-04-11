# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        N = len(nums)
        nums = sorted(nums)
        min_diff = sys.maxsize
        min_sum = 0
        for i in range(N):
            if i>0 and nums[i]== nums[i-1]:
                continue
            lo = i+1
            hi = N-1
            while lo < hi:
                _sum = nums[i]+nums[lo]+nums[hi]
                if abs(_sum-target) < min_diff:
                    min_diff = abs(_sum-target)
                    min_sum = _sum
                if _sum < target:
                    lo += 1
                else:
                    hi -= 1
        
        return min_sum
