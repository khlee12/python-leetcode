# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        # stacks
        # 每次遇到..就从stacks里pop一个元素
        stacks = []
        dirs = path.split('/')
        for each in dirs:
            if each !='' and each !='.' and each !='..':
                stacks.append(each)
            elif stacks and each == '..':
                stacks.pop()
        return '/'+'/'.join(stacks)
