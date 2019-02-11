# 55. Jump Game
# https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        # 贪心算法求最大值
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            else:
                max_reach = max(max_reach, nums[i] + i)
        return True
