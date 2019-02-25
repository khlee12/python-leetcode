# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # loop ransom note, if all char exists in magazine: true
        if ransomNote and (not magazine or magazine is None):
            return False
        
        m_chars = {}
        for i in range(len(magazine)):
            if magazine[i] in m_chars:
                m_chars[magazine[i]] += 1
            else:
                m_chars[magazine[i]] = 1
        
        for i in range(len(ransomNote)):
            if not ransomNote[i] in m_chars or m_chars[ransomNote[i]] < 1:
                return False
            else:
                m_chars[ransomNote[i]] -= 1
            
        return True
