# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 0:
            return True
        if s is None or not s:
            return False
        
        pairs = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        left_brackets = ['{', '(', '[']
        right_brackets = ['}', ')', ']']
        
        brackets_stack = []
        for i in range(len(s)):
            bracket = s[i]
            if bracket in left_brackets:
                brackets_stack.append(bracket)
            elif bracket in right_brackets:
                if len(brackets_stack) == 0:
                    return False
                pair_bracket = pairs[bracket]
                if pair_bracket == brackets_stack[-1]:
                    brackets_stack.pop()
                else:
                    return False
            else:
                continue
        
        return True if len(brackets_stack) == 0 else False
