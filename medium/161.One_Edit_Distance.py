# 161. One Edit Distance
# https://leetcode.com/problems/one-edit-distance/

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s)-len(t) > 1 or len(s)-len(t) < -1:
            return False
        
        # 1）长度一样，只有一个字符不一样 -> True
        # 2）长度相差一个, 除了多出来的字符，其余字符都一样 -> True
        ns, nt = len(s), len(t)
        min_len = min(ns, nt)
        for i in range(min_len):
            if s[i] != t[i]:
                if ns == nt:
                    # 长度一样，只有一个字符不一样
                    return s[i+1:]==t[i+1:]
                elif ns+1==nt:
                    # 长度相差一个, 除了多出来的字符，其余字符都一样
                    # 多出来的字符出现在字符串之中
                    return s[i:]==t[i+1:]
                elif nt+1==ns:
                    return s[i+1:]==t[i:]
                
        # 长度相差一个, 除了多出来的字符，其余字符都一样
        # 多出来的字符在字符串最后
        # s: "", t: "A"
        return ns+1==nt if ns<nt else nt+1==ns
