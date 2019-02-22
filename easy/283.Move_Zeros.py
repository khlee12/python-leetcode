# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# updated 2019/2/2
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # use two pointers
        # one for loop
        # the other one for representing non-zero elements boundry(what we wanted)
        non_zero_flag = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_flag],nums[i] = nums[i],nums[non_zero_flag]
                non_zero_flag += 1


# first ver.
import queue
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # init zero_pointer_queue
        # loop nums
        # if find zero number: put into zero_pointer_queue
        # else(non-zero number): 
        #   if zero_pointer_queue is not empty:
        #     get zero_pointer from queue
        #     swap zero number with non-zero number
        #     update zero_pointer_queue
        if nums is None or not nums or len(nums)==1:
            return
        
        zeroIndexes = queue.Queue()
        iterPointer = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroIndexes.put(i)
            else:
                if zeroIndexes.qsize() >= 1:
                    zeroPointer = zeroIndexes.get()
                    nums[zeroPointer], nums[i] = nums[i], nums[zeroPointer]
                    zeroIndexes.put(i)
        
