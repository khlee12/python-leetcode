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
