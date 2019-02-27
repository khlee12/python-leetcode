# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars = {}
        for i in range(len(s)):
            if s[i] in chars:
                chars[s[i]] += 1
            else:
                chars[s[i]] = 1
        for i in range(len(t)):
            if t[i] not in chars:
                return False
            else:
                chars[t[i]] -= 1
                if chars[t[i]] < 0:
                    return False
        
        return True
