# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 从右往左遍历， 如果碰到右括号在做括号的前面， swap, 直到最后变成‘（（（）））’
        # ()()() -> ()(())
        init_p = '()'*n
        result = set()

        def generate(string):
            if not string in result:
                for i in range(len(string)-1, 0, -1):
                    if string[i]=='(' and string[i-1] == ')':
                        swapped = string[:i-1]+'()'+string[i+1:]
                        generate(swapped)
                        result.add(swapped)
        generate(init_p)
        result.add(init_p)
        return list(result)
# Solution给的解法：
# 采用递归方式，添加左括号的条件是左括号数量小于 n，添加右括号的条件是右括号数小于左括号数：
# https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51525303
