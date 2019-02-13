# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        if not height or height is None or len(height)==1:
            return 0
        
        # 元素两两相比较，可以用2pointer方法
        l = 0
        r = len(height)-1
        # 最大面积
        max_area = 0
        while l < r and l < len(height) and r > -1:
            max_area = max(max_area, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return max_area
