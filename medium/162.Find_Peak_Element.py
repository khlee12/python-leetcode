# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        lo = 0
        hi = N-1
        while lo < hi:
            mid = lo+(hi-lo)//2
            if nums[mid] > nums[mid+1]:
                hi = mid #因为有可能是descending order
                # return hi
            else:
                lo = mid+1
        return lo
