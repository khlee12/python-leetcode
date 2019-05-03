# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def getStartIndex(nums):
            N = len(nums)
            lo = 0
            hi = N-1
            while lo < hi:
                mid = lo + (hi-lo)//2
                if nums[mid] > nums[mid+1]:
                    return mid+1
                elif nums[mid] >= nums[lo]:
                    lo = mid+1
                else:
                    hi = mid
            if lo == N-1:
                return 0
        
        def binarySearch(nums, left, right, target):
            lo = left
            hi = right
            while lo <= hi:
                mid = lo+(hi-lo)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    lo = mid+1
                else:
                    hi = mid-1
            return -1
        
        N = len(nums)
        if not nums:
            return -1
        if N == 1:
            return 0 if nums[0] == target else -1
        start = getStartIndex(nums)
        # print(start)
        '''
        [4,5,6,7,0,1,2] target = 3
        -> 可以分成[4,5,6,7], [0,1,2]两个范围
        if 3 < nums[0] -> 搜第二个范围
        否则搜第一个范围
        '''
        if nums[0] == target:
            return 0
        if start == 0:
            return binarySearch(nums, 0, N-1, target)
        if nums[0] > target:
            return binarySearch(nums, start, N-1, target)
        return binarySearch(nums, 0, start-1, target)
            
