# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 遇到数字： 放到stack
        # 遇到operator: 从stack里pop两个数字， 计算后将结果放到stacks
        if not tokens:
            return []
        
        operators = set(['+', '-', '*', '/'])
        stacks = []
        
        for i in range(len(tokens)):
            if not tokens[i] in operators:
                stacks.append(tokens[i])
            if tokens[i] in operators:
                num1 = int(stacks.pop())
                num2 = int(stacks.pop())
                flag = 1
                if (num1 < 0 and num2 > 0) or (num1>0 and num2<0):
                    flag = -1
                if tokens[i] == '+':
                    result = num2+num1
                elif tokens[i] == '-':
                    result = num2-num1
                elif tokens[i] == '*':
                    result = num2*num1
                elif tokens[i] == '/':
                    result = flag*(abs(num2)//abs(num1))
                stacks.append(result)
        
        return int(stacks.pop())
