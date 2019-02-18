# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        # Floyd's Tortoise and Hare (Cycle Detection)
        # 1. detect loop exist
        # 2. detect the entrance to the cycle
        
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break # loop exists
        print(tortoise)
        print(hare)
        pointer1 = nums[0]
        pointer2 = tortoise
        # find the entrance to the cycle
        while pointer1 != pointer2:
            pointer1 = nums[pointer1]
            pointer2 = nums[pointer2]
        
        return pointer1
