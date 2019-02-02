# 66. Plus One
# https://leetcode.com/problems/plus-one/

# update 2019/2/1
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None and not digits:
            return
        
        plus_flag = 1
        for i in range(len(digits)-1, -1, -1):
            temp_sum = digits[i]+plus_flag
            if temp_sum == 10:
                digits[i] = 0
                plus_flag = 1
            else:
                digits[i] = temp_sum
                plus_flag = 0
        if plus_flag == 1:
            return [plus_flag] + digits
        return digits
            
        
    
# first ver.
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None and not digits:
            return
        if len(digits) == 1:
            single_result = {
                0: [1],
                1: [2],
                2: [3],
                3: [4],
                4: [5],
                5: [6],
                6: [7],
                7: [8],
                8: [9],
                9: [1, 0]
            }
            return single_result[digits[0]]
            
        delta = 0
        temp_sum_result = []
        back_index = -1
        
        while back_index >= (-1)*len(digits):
            each_number = digits[back_index]
            temp_sum = each_number + 1 + delta if back_index == -1 else each_number + delta
            delta, rest = int(temp_sum/10), temp_sum%10
            temp_sum_result.append(rest)
            if delta == 0:
                break
            back_index -= 1
            
        result = digits[:back_index]
        if delta > 0:
            result.append(1)
        while len(temp_sum_result) > 0:
            result.append(temp_sum_result.pop())
        
        return result
        
