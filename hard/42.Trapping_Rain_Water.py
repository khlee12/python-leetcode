# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        if not height or height is None or len(height) == 1:
            return 0
        left_max = [height[0]]
        right_max = [height[-1]]
        result = 0
        
        for i in range(1, len(height)):
            left_max.append(max(height[i], left_max[-1]))
        # print(left_max)
        for i in range(len(height)-2, -1, -1):
            right_max.insert(0, max(height[i], right_max[0]))
        # print(right_max)
        for i in range(1, len(height)):
            result += min(left_max[i], right_max[i])-height[i]
        
        return result
