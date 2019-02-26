# 186. Reverse Words in a String II
# https://leetcode.com/problems/reverse-words-in-a-string-ii/
# http://www.voidcn.com/article/p-dpxpifak-qp.html

class Solution:
    def reverseWords(self, str: List[str]) -> None:
        """
        Do not return anything, modify str in-place instead.
        """
        # reverse all
        # reverse each word
        str.reverse()
        
        # use two pointer
        start = 0
        for end in range(len(str)):
            if str[end] == ' ':
                str[start:end] = reversed(str[start:end])
                start = end+1
        str[start:] = reversed(str[start:])
