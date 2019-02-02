# 31. Next Permutation
# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or not nums or len(nums) == 1:
            return

        # 字典序算法， 寻找下一个字典序列
        # 参考：https://blog.csdn.net/u011475134/article/details/75144248
        swap_index = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                swap_index = i
                break

        if swap_index > -1:
            # found it
            for j in range(len(nums)-1, -1, -1):
                if nums[j] > nums[swap_index]:
                    # swap
                    nums[swap_index], nums[j] = nums[j], nums[swap_index]
                    # 如果可以return变量的话，可以直接 return nums
                    # nums =  nums[:swap_index+1] + sorted([_ for _ in nums[swap_index+1:]])
                    # 但是这道题明示return nothing， 所以swap的方法来直接修改输入数组
                    self.reverse(nums, swap_index + 1)
                    return
        else:
            # not found
            self.reverse(nums)
            return
    def reverse(self, nums, start=0):
        end = len(nums)-1
        for i in range(start, (end+start)//2+1):
            nums[i], nums[start-i+end] = nums[start-i+end], nums[i]

