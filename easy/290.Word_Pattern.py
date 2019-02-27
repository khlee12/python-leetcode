# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # 遍历pattern and str
        # 构造一对一对应关系
        # 同一个pointer， 不同value-> False
        # 不同pointer, 同一个value-> False
        if not pattern or pattern is None:
            return False
        if not str or str is None:
            return False
        
        relates = {}
        pointer = 0
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        
        pointer = 0
        for word in words:
            if pattern[pointer] in relates:
                if relates[pattern[pointer]] != word:
                    return False
            else:
                if word in relates.values():
                    return False
                relates[pattern[pointer]] = word
            pointer += 1
        
        return True
