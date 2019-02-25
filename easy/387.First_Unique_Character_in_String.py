# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0 or s is None:
            return -1
        
        alphabet = {}
        for i in range(len(s)):
            each_char = s[i]
            if each_char in alphabet:
                alphabet[each_char].append(i)
            else:
                alphabet[each_char] = [i]
                
        min_index = -1
        for key in alphabet.keys():
            value = alphabet[key]
            if len(value) == 1:
                if min_index == -1:
                    min_index = value[0]
                else:
                    if value[0] < min_index:
                        min_index = value[0]
                        
        return min_index
