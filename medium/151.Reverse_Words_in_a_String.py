# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        if s == '':
            return s
        
        left = 0
        right = len(s)-1
        
        reverseAll = s[::-1]
        words = reverseAll.split(" ")

        result = ''
        for word in words:
            if word != '':
                result += word[::-1]+' '
        return result[:-1]
