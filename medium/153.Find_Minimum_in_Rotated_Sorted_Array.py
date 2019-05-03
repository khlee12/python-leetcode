# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        lo = 0
        hi = N-1
        while lo < hi:
            mid = lo+(hi-lo)//2
            print(mid)
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid]>= nums[lo]:
                lo = mid+1
            else:
                hi = mid
        if lo == N-1:
            # all ascending order
            return nums[0]
