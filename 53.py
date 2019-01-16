# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane Algorithm
        # https://afshinm.name/2018/06/24/why-kadane-algorithm-works/
        
        if nums is None or not nums:
            return
        if len(nums) == 1:
            return nums[0]
        
        # global_maximun
        max_so_far = nums[0]
        # 存放当前local_maximun的子数组
        elements_so_far = [nums[0]]
        
        
        for x in nums[1:]:
            if x > sum(elements_so_far + [x]):
                # 如果在当前子数组里加入x的和，还没x本身大，就将x赋值为新的子数组的起点
                # 因为加了x还比x自己小的话，没有加的意义，还不如另起一个数组
                elements_so_far = [x]
            else:
                # 否则，加入当前子数组里
                # 加了比x本身大，就加了呗，无可厚非
                elements_so_far.append(x)
            # 这个if语句可以汇成一行代码：
            # max_ending_here = max(x, max_ending_here+x)
            # max_ending_here在for循环外面初始化为nums[0]
            max_so_far = max(max_so_far, sum(elements_so_far))
        return max_so_far
    
    # 扩展题目
    # 求最大和子数组
    def maxSubArray2(self, nums):
        if nums is None or not nums:
            return
        if len(nums) == 1:
            return nums

        max_so_far = nums[0]
        elements_so_far = [nums[0]]
        # 可以用一个dict来存储最大和与最大和子数组
        states = {max_so_far: elements_so_far}

        for x in nums[1:]:

            if x > sum(elements_so_far + [x]):
                elements_so_far = [x]
            else:
                elements_so_far.append(x)

            if max_so_far < sum(elements_so_far):
                # IMPORTANT
                # 如果直接赋值用 =elements_so_far, 
                # 相当于赋值了指向elements_so_far的指针，所以elements_so_far被修改，则dict的value也会变化
                # 所以要用拷贝，来生成一个新的数组给value赋值
                states[sum(elements_so_far)] = elements_so_far[:]   
            max_so_far = max(max_so_far, sum(elements_so_far))

        return states[max_so_far]
