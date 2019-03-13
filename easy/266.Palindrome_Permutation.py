# 266. Palindrome Permutation
# https://leetcode.com/problems/palindrome-permutation/

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_count = {}
        for i in range(len(s)):
            if s[i] in char_count.keys():
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1
        
        isOdd = False
        for key in char_count.keys():
            if char_count[key] % 2 != 0:
                if isOdd:
                    return False
                else:
                    isOdd = True
        
        return True
            
            
