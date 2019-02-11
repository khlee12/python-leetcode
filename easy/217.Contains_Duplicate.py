# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        inputed = set()
        for each_num in nums:
            if each_num in inputed:
                return True
            else:
                inputed.add(each_num)
        return False
# 或者可以排序之后看是否存在一个i，使arr[i]与arr[i+1]相等
