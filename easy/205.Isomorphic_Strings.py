# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
# 题意：字符串同型分析，即需要实现s中每个字符对应着t的某个字符，并且只有一个对应；t中的每个字符对应着s中的某个字符，也只有一个对应。双向的一对一关系。
# http://zgljl2012.com/leetcode-205-isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 题意：字符串同型分析，即需要实现s中每个字符对应着t的某个字符，并且只有一个对应；t中的每个字符对应着s中的某个字符，也只有一个对应。双向的一对一关系。
        # http://zgljl2012.com/leetcode-205-isomorphic-strings/
        relations = {}
        for i in range(len(s)):
            if s[i] in relations:
                if relations[s[i]] != t[i]:
                    return False
            else:
                if t[i] in relations.values():
                    return False
                relations[s[i]] = t[i]
        
        return True
    
            
