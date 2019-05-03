# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        for num in nums1:
            if num in nums2:
                result.append(num)
        return result
