# 167. Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]
        
        lo = 0
        hi = len(numbers)-1
        while lo < hi:
            _sum = numbers[lo]+numbers[hi]
            if _sum == target:
                return [lo+1, hi+1]
            if _sum < target:
                lo += 1
            else:
                hi -= 1
        
        return [-1,-1]
