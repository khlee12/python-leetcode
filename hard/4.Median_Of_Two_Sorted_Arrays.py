# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (nums1 is None or not nums1) and (nums2 is None or not nums2):
            return 0
        
        if nums1 is None or not nums1:
            return self.findMedian(nums2)
        if nums2 is None or not nums2:
            return self.findMedian(nums1)
        
        pointer1 = 0
        pointer2 = 0
        mPointer = 0
        
        merged_array = []
                
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] < nums2[pointer2]:
                merged_array.append(nums1[pointer1])
                pointer1 += 1
            else:
                merged_array.append(nums2[pointer2])
                pointer2 += 1
            mPointer += 1
        
        while pointer1 < len(nums1):
            merged_array.append(nums1[pointer1])
            pointer1 += 1
            mPointer += 1
            
        while pointer2 < len(nums2):
            merged_array.append(nums2[pointer2])
            pointer2 += 1
            mPointer += 1
            
        return self.findMedian(merged_array)
            
    def findMedian(self, nums):
        median_index = (len(nums)-1)//2
        return nums[median_index] if len(nums)%2!=0 else ((nums[median_index]+nums[median_index+1])/2)
