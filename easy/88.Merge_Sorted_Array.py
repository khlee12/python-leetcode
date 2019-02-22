# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 从右往左遍历，由最大值开始插入
        i = m-1
        j = n-1
        m = m+n-1
        while i > -1 and j > -1:
            if nums1[i] > nums2[j]:
                nums1[m] = nums1[i]
                i -= 1
            else:
                nums1[m] = nums2[j]
                j -= 1
            m -= 1
            
        while j > -1:
            nums1[m] = nums2[j]
            j -= 1
            m -= 1
            
        
