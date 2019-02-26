# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1.
        # use array to save the indexes of vowels
        # reverse array
        # iterate char, if char is a vowel, change it with element of array
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#         v_index = []
#         for i in range(len(s)):
#             if s[i] in vowels:
#                 v_index.append(i)
                
#         v_index = v_index[::-1]
        
#         j = 0
#         result  = ''
#         for i in range(len(s)):
#             if s[i] in vowels:
#                 result += s[v_index[j]]
#                 j += 1
#             else:
#                 result += s[i]
#         return result

        # 2.
        # use two pointer, swap in place
        left = 0
        right = len(s)-1
        while left<right:
            while s[left] not in vowels and left<right:
                left += 1
            while s[right] not in vowels and left<right:
                right -= 1

            if left==right:
                return s
            s = s[:left]+s[right]+s[left+1:right]+s[left]+s[right+1:]
            left += 1
            right -= 1

        return s
